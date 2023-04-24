from fastapi import Depends
from src.repositories.observations import ObservationsRepository
from src.models.schemas.observations.observations_request import ObservationsRequest


class ObservationsService:
    def __init__(self, obs_repository: ObservationsRepository = Depends()):
        self.repo = obs_repository

    async def add(self, request: ObservationsRequest):
        return await self.repo.add(request)
