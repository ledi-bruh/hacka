from sqlalchemy import Column, String, Integer
from src.models.base import Base


class Observations(Base):
    __tablename__ = 'observations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(String, nullable=False)
