from pydantic import BaseModel


class WorkersRequest(BaseModel):
    fio: str
    address: str
    email: str
    phone_number: str
    work_exp_id: int
