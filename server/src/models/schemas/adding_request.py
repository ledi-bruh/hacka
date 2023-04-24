from pydantic import BaseModel
from typing import List
from src.models.schemas.status_request import StatusRequest


class AddingRequest(BaseModel):
    records: List[StatusRequest]
