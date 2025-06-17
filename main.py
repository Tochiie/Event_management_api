
from fastapi import FastAPI
from routes import user_routes, event_routes, speaker_routes, registration_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(event_routes.router)
app.include_router(speaker_routes.router)
app.include_router(registration_routes.router)

@app.get("/")
def root():
    return {"message": "Event Management API is running"}
