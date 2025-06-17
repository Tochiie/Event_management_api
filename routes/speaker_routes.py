from fastapi import APIRouter

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/")
def get_speakers():
    return {"message": "List of speakers"}
