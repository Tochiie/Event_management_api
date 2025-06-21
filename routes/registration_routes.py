from fastapi import APIRouter, HTTPException
from schemas.registration import RegistrationCreate, Registration
from typing import List
from datetime import date

router = APIRouter()

registrations_db = []
registration_id_counter = 1

@router.post("/", response_model=Registration, status_code=201)
def create_registration(reg: RegistrationCreate):
    global registration_id_counter
    new_registration = {
        "id": registration_id_counter,
        "user_id": reg.user_id,
        "event_id": reg.event_id,
        "registration_date": date.today(),
        "attended" : False
         
    }
    registrations_db.append(new_registration)
    registration_id_counter += 1
    return new_registration

@router.get("/{registration_id}", response_model=Registration)
def get_registration(registration_id: int):
    for reg in registrations_db:
        if reg["id"] == registration_id:
            return reg
    raise HTTPException(status_code=404, detail="Registration not found")

@router.delete("/{registration_id}", status_code=204)
def delete_registration(registration_id: int):
    for reg in registrations_db:
        if reg["id"] == registration_id:
            registrations_db.remove(reg)
            return
    raise HTTPException(status_code=404, detail="Registration not found")
