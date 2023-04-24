from fastapi import Depends
from src.repositories.workers import WorkersRepository
from src.models.schemas.workers.workers_request import WorkersRequest


class WorkersService:
    def __init__(self, repository: WorkersRepository = Depends()):
        self.repo = repository

    async def add(self, request: WorkersRequest):
        return await self.repo.add(request)
