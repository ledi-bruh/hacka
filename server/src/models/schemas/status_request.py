from pydantic import BaseModel, EmailStr


class StatusRequest(BaseModel):
    department_id: str
    fio: str
    post_name: str
    attraction_year: int
    observation_name: str
    work_status_code: str
    worker_address: str
    worker_email: EmailStr
    worker_phone_number: str
    work_exp_name: str
    work_status_status: str
