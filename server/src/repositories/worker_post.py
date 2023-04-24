from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.worker_post import WorkerPost
from src.models.schemas.worker_post.worker_post_request import WorkerPostRequest


class WorkerPostRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get(self, worker_guid: str, post_id: int) -> Optional[WorkerPost]:
        record = (
            self.session
            .query(WorkerPost)
            .filter_by(
                worker_guid=worker_guid,
                post_id=post_id,
            )
            .first()
        )
        return record

    async def add(self, request: WorkerPostRequest) -> WorkerPost:
        record = WorkerPost(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
