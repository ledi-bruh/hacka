from fastapi import APIRouter, status, Depends
from src.models.schemas.status_request import StatusRequest
from src.models.schemas.adding_request import AddingRequest


router = APIRouter(
    prefix='/status',
    tags=['status'],
)


@router.post('/', name='Добавить данные')
def get(request: AddingRequest):
    return request
