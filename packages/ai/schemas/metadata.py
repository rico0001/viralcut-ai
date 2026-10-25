from pydantic import BaseModel
from typing import List, Optional

class Metadata(BaseModel):
    title: str
    description: str
    hashtags: List[str]
    call_to_action: Optional[str] = None
    thumbnail_text: Optional[str] = None