from pydantic import BaseModel
from typing import Optional, List

class ClipBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration: float
    highlight_score: float

class ClipCreate(ClipBase):
    pass

class ClipUpdate(ClipBase):
    pass

class Clip(ClipBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True

class ClipMetadata(BaseModel):
    title: str
    description: Optional[str] = None
    hashtags: List[str] = []