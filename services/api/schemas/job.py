from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class JobBase(BaseModel):
    project_id: int
    status: str
    created_at: datetime
    updated_at: datetime

class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    status: Optional[str] = None

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class JobList(BaseModel):
    jobs: List[Job]