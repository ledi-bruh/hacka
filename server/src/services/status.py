from fastapi import Depends
from src.models.schemas.adding_request import AddingRequest
from src.models.schemas.status_request import StatusRequest

from src.repositories.posts import PostsRepository
from src.services.posts import PostsService
from src.models.schemas.posts.posts_request import PostsRequest

from src.repositories.observations import ObservationsRepository
from src.services.observations import ObservationsService
from src.models.schemas.observations.observations_request import ObservationsRequest

from src.repositories.work_exp import WorkExpRepository
from src.services.work_exp import WorkExpService
from src.models.schemas.work_exp.work_exp_request import WorkExpRequest

from src.repositories.workers import WorkersRepository
from src.services.workers import WorkersService
from src.models.schemas.workers.workers_request import WorkersRequest

from src.repositories.worker_post import WorkerPostRepository
from src.services.worker_post import WorkerPostService
from src.models.schemas.worker_post.worker_post_request import WorkerPostRequest

from src.repositories.worker_observation import WorkerObservationRepository
from src.services.worker_observation import WorkerObservationService
from src.models.schemas.worker_observation.worker_observation_request import WorkerObservationRequest

from src.repositories.work_status import WorkStatusRepository
from src.services.work_status import WorkStatusService
from src.models.schemas.work_status.work_status_request import WorkStatusRequest


class StatusService:
    def __init__(self,
                 posts_service: PostsService = Depends(),
                 posts_repo: PostsRepository = Depends(),
                 obs_service: ObservationsService = Depends(),
                 obs_repo: ObservationsRepository = Depends(),
                 work_exp_service: WorkExpService = Depends(),
                 work_exp_repo: WorkExpRepository = Depends(),
                 workers_service: WorkersService = Depends(),
                 workers_repo: WorkersRepository = Depends(),
                 worker_post_service: WorkerPostService = Depends(),
                 worker_post_repo: WorkerPostRepository = Depends(),
                 worker_obs_service: WorkerObservationService = Depends(),
                 worker_obs_repo: WorkerObservationRepository = Depends(),
                 work_status_service: WorkStatusService = Depends(),
                 work_status_repo: WorkStatusRepository = Depends()):
        self.posts_repo = posts_repo
        self.posts_service = posts_service
        self.observations_service = obs_service
        self.observations_repo = obs_repo
        self.work_exp_service = work_exp_service
        self.work_exp_repo = work_exp_repo
        self.workers_service = workers_service
        self.workers_repo = workers_repo
        self.worker_post_service = worker_post_service
        self.worker_post_repo = worker_post_repo
        self.worker_obs_service = worker_obs_service
        self.worker_obs_repo = worker_obs_repo
        self.work_status_service = work_status_service
        self.work_status_repo = work_status_repo

    async def add_all(self, request: AddingRequest) -> None:
        for record in request.records:
            await self.add(record)

    async def add(self, request: StatusRequest) -> None:
        if not (post := await self.posts_repo.get_by_name(request.post_name)):
            post = await self.posts_service.add(PostsRequest(name=request.post_name))

        if not (observation := await self.observations_repo.get(request.observation_name, request.department_id)):
            observation = await self.observations_service.add(ObservationsRequest(name=request.observation_name, department_id=request.department_id))

        if not (work_exp := await self.work_exp_repo.get_by_name(request.work_exp_name)):
            work_exp = await self.work_exp_service.add(WorkExpRequest(name=request.work_exp_name))
        
        if not (worker := await self.workers_repo.get(
            request.fio,
            request.worker_address,
            request.worker_email,
            request.worker_phone_number,
            work_exp.id,
        )):
            worker = await self.workers_service.add(WorkersRequest(
                fio=request.fio,
                address=request.worker_address,
                email=request.worker_email,
                phone_number=request.worker_phone_number,
                work_exp_id=work_exp.id,
            ))
        
        if not (await self.worker_post_repo.get(worker.guid, post.id)):
            await self.worker_post_service.add(worker.guid, post.id)
        
        if not (await self.worker_obs_repo.get(worker.guid, observation.id)):
            await self.worker_obs_service.add(worker.guid, observation.id)
        
        if not (await self.work_status_repo.get(worker.guid, post.id, request.attraction_year, observation.id, request.work_status_code)):
            await self.work_status_service.add(
                worker.guid,
                post.id,
                request.attraction_year,
                observation.id,
                request.work_status_code,
                request.work_status_status,
            )
