from pydantic import BaseModel, UUID4


class WorkerPostRequest(BaseModel):
    worker_guid = UUID4
    post_id = int
