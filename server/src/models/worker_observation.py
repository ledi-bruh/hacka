from sqlalchemy import Column, ForeignKey, Integer
from fastapi_utils.guid_type import GUID
from src.models.base import Base


class WorkerObservation(Base):
    __tablename__ = 'worker_observation'
    metadata = Base.metadata
    worker_guid = Column(GUID, ForeignKey('workers.guid', name='fk_worker_observation__worker_guid', ondelete='CASCADE'), primary_key=True)
    observation_id = Column(Integer, ForeignKey('observations.id', name='fk_worker_observation__observation_id', ondelete='CASCADE'), primary_key=True)
