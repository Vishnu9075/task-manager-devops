from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=1000)

class TaskUpdate(BaseModel):
    title: str | None = Field(min_length=1, max_length=225)
    decription: str | None = Field(default=None, max_length=1000)
    completed: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    model_config = {"from_attributes": True}