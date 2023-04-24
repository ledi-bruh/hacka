from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.observations import Observations
from src.models.schemas.observations.observations_request import ObservationsRequest


class ObservationsRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_by_name(self, name: str, department_id: str) -> Optional[Observations]:
        record = (
            self.session
            .query(Observations)
            .filter_by(name=name, department_id=department_id)
            .first()
        )
        return record

    async def add(self, request: ObservationsRequest) -> Observations:
        record = Observations(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
