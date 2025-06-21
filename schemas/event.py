from typing import Optional
from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    title: str
    location: str
    date: date
    description: str

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None 
    location: Optional[str] = None
    date: Optional[date] = None
    description: Optional[str] = None

class Event(EventBase):
    id: int
    is_open: bool = True

    class Config:
      from_attributes = True

