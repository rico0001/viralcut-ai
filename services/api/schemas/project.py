from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class ProjectList(BaseModel):
    projects: List[Project]