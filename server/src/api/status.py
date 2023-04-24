from fastapi import APIRouter, status, Depends
from src.models.schemas.adding_request import AddingRequest
from src.services.status import StatusService


router = APIRouter(
    prefix='/status',
    tags=['status'],
)


@router.post('/', status_code=status.HTTP_201_CREATED, name='Добавить данные')
async def get(request: AddingRequest, service: StatusService = Depends()):
    return await service.add_all(request)
