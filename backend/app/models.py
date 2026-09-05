from datetime import date as date_type
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Settings(SQLModel, table=True):
    """Single-row table holding the profile info needed to resolve
    age-/gender-dependent reference ranges. id is always 1."""
    id: Optional[int] = Field(default=1, primary_key=True)
    birth_year: Optional[int] = None
    gender: Optional[str] = None  # "m" or "f"
    display_name: Optional[str] = None


class Entry(SQLModel, table=True):
    """One lab report / blood draw on a given date."""
    id: Optional[int] = Field(default=None, primary_key=True)
    entry_date: date_type
    lab_name: Optional[str] = None
    note: Optional[str] = None
    photo_path: Optional[str] = None  # reserved for a later OCR/photo-upload step

    measurements: List["Measurement"] = Relationship(
        back_populates="entry",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


class ParameterOverride(SQLModel, table=True):
    """Lets the user override the built-in reference range for a parameter,
    e.g. to match the exact range printed on their own lab's reports."""
    parameter_code: str = Field(primary_key=True)
    low: Optional[float] = None
    high: Optional[float] = None


class Measurement(SQLModel, table=True):
    """A single measured value (e.g. GGT = 34 U/l) belonging to one entry."""
    id: Optional[int] = Field(default=None, primary_key=True)
    entry_id: int = Field(foreign_key="entry.id")
    parameter_code: str
    value: float
    unit_override: Optional[str] = None  # in case a lab uses a different unit

    entry: Optional[Entry] = Relationship(back_populates="measurements")
