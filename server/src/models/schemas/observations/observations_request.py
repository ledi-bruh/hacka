from pydantic import BaseModel


class ObservationsRequest(BaseModel):
    name: str
    department_id: str
