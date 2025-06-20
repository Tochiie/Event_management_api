from fastapi import APIRouter
from schemas.speaker import SpeakerCreate, Speaker

router = APIRouter()

@router.post("/", response_model=Speaker, status_code=201)
def create_speaker(speaker: SpeakerCreate):
    return {
        "id": 1,
        "name": speaker.name,
        "topic": speaker.topic
    }
