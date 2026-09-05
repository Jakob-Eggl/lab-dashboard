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
