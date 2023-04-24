from fastapi import Depends
from src.repositories.work_exp import WorkExpRepository
from src.models.schemas.work_exp.work_exp_request import WorkExpRequest


class WorkExpService:
    def __init__(self, repository: WorkExpRepository = Depends()):
        self.repo = repository

    async def add(self, request: WorkExpRequest):
        return await self.repo.add(request)
