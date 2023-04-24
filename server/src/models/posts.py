from sqlalchemy import Column, String, Integer
from src.models.base import Base


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
