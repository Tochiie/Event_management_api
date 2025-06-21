from fastapi import APIRouter, HTTPException
from schemas.event import EventCreate, Event
from typing import List

router = APIRouter()

events_db = []
event_id_counter = 1

@router.post("/", response_model=Event, status_code=201)
def create_event(event: EventCreate):
    global event_id_counter
    new_event = {
        "id": event_id_counter,
        "title": event.title,
        "location": event.location,
        "description": event.description,
        "date": event.date
    }
    events_db.append(new_event)
    event_id_counter += 1
    return new_event

@router.get("/", response_model=List[Event])
def get_events():
    return events_db

@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int):
    for event in events_db:
        if event["id"] == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, updated: EventCreate):
    for event in events_db:
        if event["id"] == event_id:
            event["title"] = updated.title
            event["description"] = updated.description
            event["date"] = updated.date
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int):
    for event in events_db:
        if event["id"] == event_id:
            events_db.remove(event)
            return
    raise HTTPException(status_code=404, detail="Event not found")
