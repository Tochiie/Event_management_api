
from data.db import events
from schemas.event import Event, EventCreate

def create_event(event_data: EventCreate):
    event_id = len(events) + 1
    new_event = Event(id=event_id, **event_data.dict())
    events.append(new_event)
    return new_event

def get_event(event_id: int):
    return next((e for e in events if e.id == event_id), None)

def get_events():
    return events

def close_event(event_id: int):
    event = get_event(event_id)
    if event:
        event.is_open = False
    return event
