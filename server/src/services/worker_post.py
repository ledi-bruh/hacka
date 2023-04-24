from fastapi import Depends
from src.repositories.worker_post import WorkerPostRepository
from src.models.schemas.worker_post.worker_post_request import WorkerPostRequest


class WorkerPostService:
    def __init__(self, repository: WorkerPostRepository = Depends()):
        self.repo = repository

    async def add(self, worker_guid: str, post_id: int):
        return await self.repo.add(worker_guid, post_id)
