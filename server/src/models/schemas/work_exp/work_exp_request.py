from pydantic import BaseModel


class WorkExpRequest(BaseModel):
    name: str
