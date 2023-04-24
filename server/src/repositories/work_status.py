from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.work_status import WorkStatus
from src.models.schemas.work_status.work_status_request import WorkStatusRequest


class WorkStatusRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get(self, worker_guid: str, post_id: int, attraction_year: int, observation_id: int, code: str) -> Optional[WorkStatus]:
        record = (
            self.session
            .query(WorkStatus)
            .filter_by(
                worker_guid=worker_guid,
                post_id=post_id,
                attraction_year=attraction_year,
                observation_id=observation_id,
                code=code,
            )
            .first()
        )
        return record

    async def add(self, worker_guid: str, post_id: int, attraction_year: int, observation_id: int, work_status_code: str, work_status_status: str) -> WorkStatus:
        record = WorkStatus(
            worker_guid=worker_guid,
            post_id=post_id,
            attraction_year=attraction_year,
            observation_id=observation_id,
            code=work_status_code,
            status=work_status_status
        )
        self.session.add(record)
        self.session.commit()
        return record
