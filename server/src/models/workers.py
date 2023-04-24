from sqlalchemy import Column, String, Integer, ForeignKey
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from src.models.base import Base


class Workers(Base):
    __tablename__ = 'workers'
    guid = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    fio = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    work_exp_id = Column(Integer, ForeignKey('work_exp.id', name='fk_workers__work_exp_id', ondelete='CASCADE'), nullable=False)
