from sqlalchemy import Column, String, Integer, ForeignKey
from fastapi_utils.guid_type import GUID
from src.models.base import Base


class WorkStatus(Base):
    __tablename__ = 'work_status'
    worker_guid = Column(GUID, ForeignKey('workers.guid', name='fk_work_status__worker_guid', ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', name='fk_work_status__post_id', ondelete='CASCADE'), primary_key=True)
    attraction_year = Column(Integer, primary_key=True)
    observation_id = Column(Integer, ForeignKey('observations.id', name='fk_work_status__observation_id', ondelete='CASCADE'), primary_key=True)
    code = Column(String, primary_key=True)
    status = Column(String, nullable=False)
