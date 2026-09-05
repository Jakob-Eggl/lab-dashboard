from datetime import date as date_type
from typing import Optional, List
from pydantic import BaseModel


class MeasurementIn(BaseModel):
    parameter_code: str
    value: float
    unit_override: Optional[str] = None


class MeasurementOut(BaseModel):
    id: int
    parameter_code: str
    value: float
    unit_override: Optional[str] = None


class EntryIn(BaseModel):
    entry_date: date_type
    lab_name: Optional[str] = None
    note: Optional[str] = None
    measurements: List[MeasurementIn]


class EntryOut(BaseModel):
    id: int
    entry_date: date_type
    lab_name: Optional[str] = None
    note: Optional[str] = None
    measurements: List[MeasurementOut]


class SettingsIn(BaseModel):
    birth_year: Optional[int] = None
    gender: Optional[str] = None  # "m" | "f"
    display_name: Optional[str] = None


class SettingsOut(SettingsIn):
    pass


class ParameterOut(BaseModel):
    code: str
    name: str
    full_name: str
    unit: str
    category: str
    description: str
    high_meaning: str
    low_meaning: str
    reference_low: Optional[float] = None
    reference_high: Optional[float] = None
    default_low: Optional[float] = None
    default_high: Optional[float] = None
    default_unit: str
    is_custom_range: bool = False
    is_custom_unit: bool = False
    computed: bool = False


class ParameterOverrideIn(BaseModel):
    low: Optional[float] = None
    high: Optional[float] = None
    unit: Optional[str] = None


class ParameterOverrideOut(BaseModel):
    parameter_code: str
    low: Optional[float] = None
    high: Optional[float] = None
    unit: Optional[str] = None


class DashboardItem(BaseModel):
    parameter: ParameterOut
    latest_value: Optional[float] = None
    latest_date: Optional[date_type] = None
    unit: str
    status: str  # "low" | "normal" | "high" | "unknown"
    previous_value: Optional[float] = None


class HistoryPoint(BaseModel):
    date: date_type
    value: float
    entry_id: int


class HistoryOut(BaseModel):
    parameter: ParameterOut
    points: List[HistoryPoint]


class ExportData(BaseModel):
    exported_at: str
    version: int = 1
    settings: SettingsOut
    parameter_overrides: List[ParameterOverrideOut]
    entries: List[EntryIn]
