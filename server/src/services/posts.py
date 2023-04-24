from fastapi import Depends
from src.repositories.posts import PostsRepository
from src.models.schemas.posts.posts_request import PostsRequest


class PostsService:
    def __init__(self, posts_repository: PostsRepository = Depends()):
        self.repo = posts_repository

    async def add(self, request: PostsRequest):
        return await self.repo.add(request)
