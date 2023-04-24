from fastapi import APIRouter, status, Depends
from src.models.schemas.adding_request import AddingRequest
from src.models.schemas.query_request import QueryRequest
from src.services.status import StatusService


router = APIRouter(
    prefix='/status',
    tags=['status'],
)


@router.post('/', status_code=status.HTTP_201_CREATED, name='Добавить данные')
async def get(request: AddingRequest, service: StatusService = Depends()):
    print(request.records)
    print('===========')
    return await service.add_all(request)


@router.post('/filter', status_code=status.HTTP_201_CREATED, name='Получить выборку')
async def get(request: QueryRequest, service: StatusService = Depends()):
    return await service.get_by_query(request.query)
