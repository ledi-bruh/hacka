from sqlalchemy import Column, String, Integer
from src.models.base import Base


class WorkExp(Base):
    __tablename__ = 'work_exp'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
