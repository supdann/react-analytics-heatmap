from fastapi import APIRouter

from app.api import initial_v1

api_router = APIRouter()

api_router.include_router(initial_v1.router, tags=["Initial"])

tags_metadata = [
    {"name": "CV2-Service", "description": "CV2 Service"},
]
