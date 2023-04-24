from fastapi import APIRouter
from src.api import status


base_router = APIRouter()
base_router.include_router(status.router)
