from pydantic import BaseModel, UUID4


class WorkStatusRequest(BaseModel):
    worker_guid = UUID4
    post_id = int
    attraction_year = int
    observation_id = int
    code = str
    status = str
