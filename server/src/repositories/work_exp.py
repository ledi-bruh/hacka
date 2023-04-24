from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.work_exp import WorkExp
from src.models.schemas.work_exp.work_exp_request import WorkExpRequest


class WorkExpRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_by_name(self, name: str) -> Optional[WorkExp]:
        record = (
            self.session
            .query(WorkExp)
            .filter_by(name=name)
            .first()
        )
        return record

    async def add(self, request: WorkExpRequest) -> WorkExp:
        record = WorkExp(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
