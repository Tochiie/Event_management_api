from data.db import registrations, users, events
from schemas.registration import Registration
from datetime import datetime

def register_user(user_id: int, event_id: int):
    if any(r.user_id == user_id and r.event_id == event_id for r in registrations):
        return None  # Already registered
    
    user = next((u for u in users if u.id == user_id and u.is_active), None)
    event = next((e for e in events if e.id == event_id and e.is_open), None)

    if user and event:
        reg_id = len(registrations) + 1
        reg = Registration(
            id=reg_id,
            user_id=user_id,
            event_id=event_id,
            registration_date=datetime.now(),
            attended=False
        )
        registrations.append(reg)
        return reg
    return None

def get_user_registrations(user_id: int):
    return [r for r in registrations if r.user_id == user_id]

def get_all_registrations():
    return registrations

def mark_attendance(registration_id: int):
    reg = next((r for r in registrations if r.id == registration_id), None)
    if reg:
        reg.attended = True
    return reg
