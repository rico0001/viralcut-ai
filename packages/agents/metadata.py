from pydantic import BaseModel
from typing import List, Optional

class Metadata(BaseModel):
    title: str
    description: str
    hashtags: List[str]
    call_to_action: Optional[str] = None
    thumbnail_text: Optional[str] = None

class MetadataGenerator:
    def generate_metadata(self, clip_title: str, clip_description: str, clip_hashtags: List[str]) -> Metadata:
        return Metadata(
            title=clip_title,
            description=clip_description,
            hashtags=clip_hashtags
        )