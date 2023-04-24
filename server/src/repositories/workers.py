from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.workers import Workers
from src.models.schemas.workers.workers_request import WorkersRequest


class WorkersRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get(self, fio: str, address: str, email: str, phone_number: str, work_exp_id: int) -> Optional[Workers]:
        record = (
            self.session
            .query(Workers)
            .filter_by(
                fio=fio,
                address=address,
                email=email,
                phone_number=phone_number,
                work_exp_id=work_exp_id,
            )
            .first()
        )
        return record

    async def add(self, request: WorkersRequest) -> Workers:
        record = Workers(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
