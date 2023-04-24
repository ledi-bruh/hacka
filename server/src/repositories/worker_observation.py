from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session
from src.models.worker_observation import WorkerObservation
from src.models.schemas.worker_observation.worker_observation_request import WorkerObservationRequest


class WorkerObservationRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get(self, worker_guid: str, observation_id: int) -> Optional[WorkerObservation]:
        record = (
            self.session
            .query(WorkerObservation)
            .filter_by(
                worker_guid=worker_guid,
                observation_id=observation_id,
            )
            .first()
        )
        return record

    async def add(self, request: WorkerObservationRequest) -> WorkerObservation:
        record = WorkerObservation(**dict(request))
        self.session.add(record)
        self.session.commit()
        return record
