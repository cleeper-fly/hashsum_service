from fastapi import APIRouter

from app.apps.file_hash.api import router as hash_router
from app.core.config import get_settings

config = get_settings()

v1_routers: tuple[APIRouter, ...] = (
    hash_router,
)
