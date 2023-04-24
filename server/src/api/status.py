from fastapi import APIRouter, status, Depends
from src.models.schemas.adding_request import AddingRequest


router = APIRouter(
    prefix='/status',
    tags=['status'],
)


@router.post('/', name='Добавить данные')
async def get(request: AddingRequest):
    return request
