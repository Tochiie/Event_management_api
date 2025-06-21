from fastapi import APIRouter, HTTPException
from schemas.user import User, UserCreate, UserUpdate
from services.user_service import users_db

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate):
    if any(u.email == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = User(id=len(users_db) + 1, name=user.name, email=user.email, is_active=True)
    users_db.append(new_user)
    return new_user

@router.get("/", response_model=list[User])
def get_all_users():
    return users_db

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, data: UserUpdate):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if data.name:
        user.name = data.name
    if data.email:
        if any(u.email == data.email and u.id != user_id for u in users_db):
            raise HTTPException(status_code=400, detail="Email already exists")
        user.email = data.email
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    global users_db
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users_db = [u for u in users_db if u.id != user_id]
    return {"detail": "User deleted"}

@router.put("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = False
    return {"detail": "User deactivated"}
