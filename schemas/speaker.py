# schemas/speaker.py

from pydantic import BaseModel

class SpeakerBase(BaseModel):
    name: str
    topic: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int

    class Config:
        orm_mode = True
