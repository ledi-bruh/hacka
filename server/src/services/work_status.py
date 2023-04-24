from fastapi import Depends
from src.repositories.work_status import WorkStatusRepository
from src.models.schemas.work_status.work_status_request import WorkStatusRequest


class WorkStatusService:
    def __init__(self, repository: WorkStatusRepository = Depends()):
        self.repo = repository

    async def add(self, worker_guid: str, post_id: int, attraction_year: int, observation_id: int, work_status_code: str, work_status_status: str):
        return await self.repo.add(worker_guid, post_id, attraction_year, observation_id, work_status_code, work_status_status)
