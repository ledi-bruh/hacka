from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.posts import Posts
from src.models.schemas.posts.posts_request import PostsRequest


class PostsRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_by_name(self, name: str) -> Optional[PostsRequest]:
        record = (
            self.session
            .query(Posts)
            .filter_by(name=name)
            .first()
        )
        return record

    async def add(self, request: PostsRequest) -> Posts:
        record = Posts(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
