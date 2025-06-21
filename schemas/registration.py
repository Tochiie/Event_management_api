from pydantic import BaseModel
from datetime import date

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: int
    registration_date: date
    attended: bool

    class Config:
      from_attributes = True

