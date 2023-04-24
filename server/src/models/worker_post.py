from sqlalchemy import Column, ForeignKey, Integer
from fastapi_utils.guid_type import GUID
from src.models.base import Base


class WorkerPost(Base):
    __tablename__ = 'worker_post'
    metadata = Base.metadata
    worker_guid = Column(GUID, ForeignKey('workers.guid', name='fk_worker_post__worker_guid', ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', name='fk_worker_post__post_id', ondelete='CASCADE'), primary_key=True)
