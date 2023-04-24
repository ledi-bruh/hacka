from pydantic import BaseModel


class PostsRequest(BaseModel):
    name: str
