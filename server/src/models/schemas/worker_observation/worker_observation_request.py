from pydantic import BaseModel, UUID4


class WorkerObservationRequest(BaseModel):
    worker_guid = UUID4
    observation_id = int
