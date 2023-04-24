from fastapi import Depends
from src.repositories.worker_observation import WorkerObservationRepository
from src.models.schemas.worker_observation.worker_observation_request import WorkerObservationRequest


class WorkerObservationService:
    def __init__(self, repository: WorkerObservationRepository = Depends()):
        self.repo = repository

    async def add(self, worker_guid: str, observation_id: int):
        return await self.repo.add(worker_guid, observation_id)
