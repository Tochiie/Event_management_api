from fastapi import FastAPI
from routes import speaker_routes, user_routes, event_routes, registration_routes

app = FastAPI()

app.include_router(speaker_routes.router, prefix="/speakers", tags=["Speakers"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(event_routes.router, prefix="/events", tags=["Events"])
app.include_router(registration_routes.router, prefix="/registrations", tags=["Registrations"])
