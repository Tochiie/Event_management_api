from fastapi import APIRouter

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/")
def get_registrations():
    return {"message": "List of registrations"}
