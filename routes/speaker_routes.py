from fastapi import APIRouter, HTTPException
from schemas.speaker import SpeakerCreate, Speaker
from typing import List

router = APIRouter()

speakers_db = []
speaker_id_counter = 1

@router.post("/", response_model=Speaker, status_code=201)
def create_speaker(speaker: SpeakerCreate):
    global speaker_id_counter
    new_speaker = {"id": speaker_id_counter, "name": speaker.name, "topic": speaker.topic}
    speakers_db.append(new_speaker)
    speaker_id_counter += 1
    return new_speaker

@router.get("/{speaker_id}", response_model=Speaker)
def get_speaker(speaker_id: int):
    for speaker in speakers_db:
        if speaker["id"] == speaker_id:
            return speaker
    raise HTTPException(status_code=404, detail="Speaker not found")

@router.put("/{speaker_id}", response_model=Speaker)
def update_speaker(speaker_id: int, updated: SpeakerCreate):
    for speaker in speakers_db:
        if speaker["id"] == speaker_id:
            speaker["name"] = updated.name
            speaker["topic"] = updated.topic
            return speaker
    raise HTTPException(status_code=404, detail="Speaker not found")

@router.delete("/{speaker_id}", status_code=204)
def delete_speaker(speaker_id: int):
    for speaker in speakers_db:
        if speaker["id"] == speaker_id:
            speakers_db.remove(speaker)
            return
    raise HTTPException(status_code=404, detail="Speaker not found")
