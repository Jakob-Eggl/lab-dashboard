from datetime import date
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from .database import init_db, get_session, engine
from .models import Entry, Measurement, Settings
from .schemas import (
    EntryIn, EntryOut, MeasurementOut, SettingsIn, SettingsOut,
    ParameterOut, DashboardItem, HistoryOut, HistoryPoint,
)
from .parameters_data import PARAMETERS, PARAMETERS_BY_CODE, resolve_range

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


def _param_out(code: str, age_years: Optional[int], gender: Optional[str]) -> ParameterOut:
    p = PARAMETERS_BY_CODE[code]
    rng = resolve_range(code, age_years, gender)
    return ParameterOut(
        code=p["code"],
        name=p["name"],
        full_name=p["full_name"],
        unit=p["unit"],
        category=p["category"],
        description=p["description"],
        high_meaning=p["high_meaning"],
        low_meaning=p["low_meaning"],
        reference_low=rng["low"] if rng else None,
        reference_high=rng["high"] if rng else None,
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
    return [_param_out(p["code"], age, s.gender) for p in PARAMETERS]


# ---------------------------------------------------------------- Entries
@app.get("/api/entries", response_model=List[EntryOut])
def list_entries(session: Session = Depends(get_session)):
    entries = session.exec(select(Entry).order_by(Entry.entry_date.desc())).all()
    out = []
    for e in entries:
        out.append(EntryOut(
            id=e.id,
            entry_date=e.entry_date,
            lab_name=e.lab_name,
            note=e.note,
            measurements=[
                MeasurementOut(id=m.id, parameter_code=m.parameter_code, value=m.value, unit_override=m.unit_override)
                for m in e.measurements
            ],
        ))
    return out


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
        param_out = _param_out(code, age, s.gender)
        if not points:
            items.append(DashboardItem(
                parameter=param_out, latest_value=None, latest_date=None,
                unit=p["unit"], status="unknown", previous_value=None,
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
            unit=p["unit"],
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

    return HistoryOut(parameter=_param_out(parameter_code, age, s.gender), points=points)


@app.get("/api/health")
def health():
    return {"status": "ok"}
