from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.db import get_session


class StatusRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_by_query(self, query: str):
        result = self.session.execute(query)
        return result
