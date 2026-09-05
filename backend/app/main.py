from datetime import date, datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from .database import init_db, get_session, engine
from .models import Entry, Measurement, Settings, ParameterOverride
from .schemas import (
    EntryIn, EntryOut, MeasurementOut, SettingsIn, SettingsOut,
    ParameterOut, DashboardItem, HistoryOut, HistoryPoint,
    ParameterOverrideIn, ParameterOverrideOut, ExportData,
)
from .parameters_data import PARAMETERS, PARAMETERS_BY_CODE, resolve_range

HEIGHT_CODE = "groesse"
WEIGHT_CODE = "gewicht"
BMI_CODE = "bmi"

app = FastAPI(title="Laborwerte Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()
    # make sure the settings singleton row exists
    with Session(engine) as session:
        _get_or_create_settings(session)


def _get_or_create_settings(session: Session) -> Settings:
    settings = session.get(Settings, 1)
    if not settings:
        settings = Settings(id=1)
        session.add(settings)
        session.commit()
        session.refresh(settings)
    return settings


def _age_years(birth_year: Optional[int]) -> Optional[int]:
    if not birth_year:
        return None
    return date.today().year - birth_year


def _param_out(code: str, age_years: Optional[int], gender: Optional[str], session: Session) -> ParameterOut:
    p = PARAMETERS_BY_CODE[code]
    rng = resolve_range(code, age_years, gender)
    default_low = rng["low"] if rng else None
    default_high = rng["high"] if rng else None
    default_unit = p["unit"]

    override = session.get(ParameterOverride, code)
    has_range_override = override is not None and (override.low is not None or override.high is not None)
    has_unit_override = override is not None and bool(override.unit)

    low = override.low if (has_range_override and override.low is not None) else default_low
    high = override.high if (has_range_override and override.high is not None) else default_high
    unit = override.unit if has_unit_override else default_unit

    return ParameterOut(
        code=p["code"],
        name=p["name"],
        full_name=p["full_name"],
        unit=unit,
        category=p["category"],
        description=p["description"],
        high_meaning=p["high_meaning"],
        low_meaning=p["low_meaning"],
        reference_low=low,
        reference_high=high,
        default_low=default_low,
        default_high=default_high,
        default_unit=default_unit,
        is_custom_range=has_range_override,
        is_custom_unit=has_unit_override,
        computed=bool(p.get("computed", False)),
    )


def _apply_bmi(entry: Entry, session: Session):
    """If both height (groesse, cm) and weight (gewicht, kg) are present on
    this entry, (re)compute the bmi measurement automatically."""
    height = next((m for m in entry.measurements if m.parameter_code == HEIGHT_CODE), None)
    weight = next((m for m in entry.measurements if m.parameter_code == WEIGHT_CODE), None)
    existing_bmi = next((m for m in entry.measurements if m.parameter_code == BMI_CODE), None)

    if height and weight and height.value and weight.value:
        height_m = height.value / 100.0
        bmi_value = round(weight.value / (height_m ** 2), 1)
        if existing_bmi:
            existing_bmi.value = bmi_value
            session.add(existing_bmi)
        else:
            session.add(Measurement(entry_id=entry.id, parameter_code=BMI_CODE, value=bmi_value))
        session.commit()
    elif existing_bmi and not (height and weight):
        # height or weight was removed again -> drop the stale computed value
        session.delete(existing_bmi)
        session.commit()


def _entry_out(entry: Entry) -> EntryOut:
    return EntryOut(
        id=entry.id,
        entry_date=entry.entry_date,
        lab_name=entry.lab_name,
        note=entry.note,
        measurements=[
            MeasurementOut(id=m.id, parameter_code=m.parameter_code, value=m.value, unit_override=m.unit_override)
            for m in entry.measurements
        ],
    )


# ---------------------------------------------------------------- Settings
@app.get("/api/settings", response_model=SettingsOut)
def get_settings(session: Session = Depends(get_session)):
    s = _get_or_create_settings(session)
    return SettingsOut(birth_year=s.birth_year, gender=s.gender, display_name=s.display_name)


@app.put("/api/settings", response_model=SettingsOut)
def update_settings(data: SettingsIn, session: Session = Depends(get_session)):
    s = _get_or_create_settings(session)
    s.birth_year = data.birth_year
    s.gender = data.gender
    s.display_name = data.display_name
    session.add(s)
    session.commit()
    session.refresh(s)
    return SettingsOut(birth_year=s.birth_year, gender=s.gender, display_name=s.display_name)


# ---------------------------------------------------------------- Parameters
@app.get("/api/parameters", response_model=List[ParameterOut])
def list_parameters(session: Session = Depends(get_session)):
    s = _get_or_create_settings(session)
    age = _age_years(s.birth_year)
    return [_param_out(p["code"], age, s.gender, session) for p in PARAMETERS]


# ------------------------------------------------------- Reference range overrides
@app.get("/api/parameter-overrides", response_model=List[ParameterOverrideOut])
def list_overrides(session: Session = Depends(get_session)):
    overrides = session.exec(select(ParameterOverride)).all()
    return [
        ParameterOverrideOut(parameter_code=o.parameter_code, low=o.low, high=o.high, unit=o.unit)
        for o in overrides
    ]


@app.put("/api/parameter-overrides/{parameter_code}", response_model=ParameterOverrideOut)
def set_override(parameter_code: str, data: ParameterOverrideIn, session: Session = Depends(get_session)):
    if parameter_code not in PARAMETERS_BY_CODE:
        raise HTTPException(404, "Unbekannter Parameter")
    override = session.get(ParameterOverride, parameter_code)

    unit = data.unit.strip() if data.unit else None
    # a unit equal to the catalog default doesn't need to be stored as an override
    if unit and unit == PARAMETERS_BY_CODE[parameter_code]["unit"]:
        unit = None

    if data.low is None and data.high is None and unit is None:
        # nothing to store -> remove any existing override, reset to default
        if override:
            session.delete(override)
            session.commit()
        return ParameterOverrideOut(parameter_code=parameter_code, low=None, high=None, unit=None)

    if not override:
        override = ParameterOverride(parameter_code=parameter_code)
    override.low = data.low
    override.high = data.high
    override.unit = unit
    session.add(override)
    session.commit()
    session.refresh(override)
    return ParameterOverrideOut(parameter_code=override.parameter_code, low=override.low, high=override.high, unit=override.unit)


@app.delete("/api/parameter-overrides/{parameter_code}")
def delete_override(parameter_code: str, session: Session = Depends(get_session)):
    override = session.get(ParameterOverride, parameter_code)
    if override:
        session.delete(override)
        session.commit()
    return {"ok": True}


# ---------------------------------------------------------------- Entries
@app.get("/api/entries", response_model=List[EntryOut])
def list_entries(session: Session = Depends(get_session)):
    entries = session.exec(select(Entry).order_by(Entry.entry_date.desc())).all()
    return [_entry_out(e) for e in entries]


@app.post("/api/entries", response_model=EntryOut)
def create_entry(data: EntryIn, session: Session = Depends(get_session)):
    unknown = [m.parameter_code for m in data.measurements if m.parameter_code not in PARAMETERS_BY_CODE]
    if unknown:
        raise HTTPException(400, f"Unbekannte Parameter-Codes: {unknown}")

    entry = Entry(entry_date=data.entry_date, lab_name=data.lab_name, note=data.note)
    session.add(entry)
    session.commit()
    session.refresh(entry)

    for m in data.measurements:
        session.add(Measurement(
            entry_id=entry.id,
            parameter_code=m.parameter_code,
            value=m.value,
            unit_override=m.unit_override,
        ))
    session.commit()
    session.refresh(entry)
    _apply_bmi(entry, session)
    session.refresh(entry)

    return _entry_out(entry)


@app.put("/api/entries/{entry_id}", response_model=EntryOut)
def update_entry(entry_id: int, data: EntryIn, session: Session = Depends(get_session)):
    entry = session.get(Entry, entry_id)
    if not entry:
        raise HTTPException(404, "Eintrag nicht gefunden")
    unknown = [m.parameter_code for m in data.measurements if m.parameter_code not in PARAMETERS_BY_CODE]
    if unknown:
        raise HTTPException(400, f"Unbekannte Parameter-Codes: {unknown}")

    entry.entry_date = data.entry_date
    entry.lab_name = data.lab_name
    entry.note = data.note

    for m in list(entry.measurements):
        session.delete(m)
    session.commit()

    for m in data.measurements:
        session.add(Measurement(
            entry_id=entry.id,
            parameter_code=m.parameter_code,
            value=m.value,
            unit_override=m.unit_override,
        ))
    session.add(entry)
    session.commit()
    session.refresh(entry)
    _apply_bmi(entry, session)
    session.refresh(entry)

    return _entry_out(entry)


@app.delete("/api/entries/{entry_id}")
def delete_entry(entry_id: int, session: Session = Depends(get_session)):
    entry = session.get(Entry, entry_id)
    if not entry:
        raise HTTPException(404, "Eintrag nicht gefunden")
    session.delete(entry)
    session.commit()
    return {"ok": True}


# ---------------------------------------------------------------- Dashboard & history
@app.get("/api/dashboard", response_model=List[DashboardItem])
def dashboard(session: Session = Depends(get_session)):
    s = _get_or_create_settings(session)
    age = _age_years(s.birth_year)

    entries = session.exec(select(Entry).order_by(Entry.entry_date.desc())).all()

    # collect, per parameter code, the sorted (date, value) history
    history: dict[str, list[tuple[date, float]]] = {p["code"]: [] for p in PARAMETERS}
    for e in entries:  # already sorted desc by date
        for m in e.measurements:
            history.setdefault(m.parameter_code, []).append((e.entry_date, m.value))

    items = []
    for p in PARAMETERS:
        code = p["code"]
        points = history.get(code, [])
        param_out = _param_out(code, age, s.gender, session)
        if not points:
            items.append(DashboardItem(
                parameter=param_out, latest_value=None, latest_date=None,
                unit=param_out.unit, status="unknown", previous_value=None,
            ))
            continue

        latest_date, latest_value = points[0]
        previous_value = points[1][1] if len(points) > 1 else None

        status = "unknown"
        if param_out.reference_low is not None and param_out.reference_high is not None:
            if latest_value < param_out.reference_low:
                status = "low"
            elif latest_value > param_out.reference_high:
                status = "high"
            else:
                status = "normal"

        items.append(DashboardItem(
            parameter=param_out,
            latest_value=latest_value,
            latest_date=latest_date,
            unit=param_out.unit,
            status=status,
            previous_value=previous_value,
        ))

    return items


@app.get("/api/history/{parameter_code}", response_model=HistoryOut)
def history(parameter_code: str, session: Session = Depends(get_session)):
    if parameter_code not in PARAMETERS_BY_CODE:
        raise HTTPException(404, "Unbekannter Parameter")
    s = _get_or_create_settings(session)
    age = _age_years(s.birth_year)

    rows = session.exec(
        select(Measurement, Entry)
        .where(Measurement.entry_id == Entry.id)
        .where(Measurement.parameter_code == parameter_code)
        .order_by(Entry.entry_date.asc())
    ).all()

    points = [HistoryPoint(date=e.entry_date, value=m.value, entry_id=e.id) for m, e in rows]

    return HistoryOut(parameter=_param_out(parameter_code, age, s.gender, session), points=points)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------- Export / Import
@app.get("/api/export", response_model=ExportData)
def export_data(session: Session = Depends(get_session)):
    s = _get_or_create_settings(session)
    overrides = session.exec(select(ParameterOverride)).all()
    entries = session.exec(select(Entry).order_by(Entry.entry_date.asc())).all()

    return ExportData(
        exported_at=datetime.utcnow().isoformat(),
        settings=SettingsOut(birth_year=s.birth_year, gender=s.gender, display_name=s.display_name),
        parameter_overrides=[
            ParameterOverrideOut(parameter_code=o.parameter_code, low=o.low, high=o.high, unit=o.unit)
            for o in overrides
        ],
        entries=[
            EntryIn(
                entry_date=e.entry_date,
                lab_name=e.lab_name,
                note=e.note,
                measurements=[
                    {"parameter_code": m.parameter_code, "value": m.value, "unit_override": m.unit_override}
                    for m in e.measurements
                ],
            )
            for e in entries
        ],
    )


@app.post("/api/import")
def import_data(data: ExportData, session: Session = Depends(get_session)):
    """Full restore from an export file. This REPLACES all current data,
    so the frontend must ask the user to confirm before calling this."""
    # wipe existing data
    for e in session.exec(select(Entry)).all():
        session.delete(e)
    for o in session.exec(select(ParameterOverride)).all():
        session.delete(o)
    session.commit()

    s = _get_or_create_settings(session)
    s.birth_year = data.settings.birth_year
    s.gender = data.settings.gender
    s.display_name = data.settings.display_name
    session.add(s)

    for o in data.parameter_overrides:
        if o.parameter_code in PARAMETERS_BY_CODE:
            session.add(ParameterOverride(parameter_code=o.parameter_code, low=o.low, high=o.high, unit=o.unit))

    session.commit()  # persist settings + overrides even if there are no entries at all

    imported, skipped = 0, 0
    for entry_data in data.entries:
        measurements = [m for m in entry_data.measurements if m.parameter_code in PARAMETERS_BY_CODE]
        skipped += len(entry_data.measurements) - len(measurements)
        entry = Entry(entry_date=entry_data.entry_date, lab_name=entry_data.lab_name, note=entry_data.note)
        session.add(entry)
        session.commit()
        session.refresh(entry)
        for m in measurements:
            session.add(Measurement(
                entry_id=entry.id, parameter_code=m.parameter_code,
                value=m.value, unit_override=m.unit_override,
            ))
        session.commit()
        imported += 1

    return {"ok": True, "imported_entries": imported, "skipped_measurements": skipped}
