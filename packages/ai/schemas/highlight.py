from pydantic import BaseModel
from typing import List, Optional

class Highlight(BaseModel):
    start_timestamp: float
    end_timestamp: float
    title: str
    explanation: str
    primary_topic: str
    hook: str
    supporting_evidence: str
    engagement_potential: float
    confidence_score: float
    context_warnings: Optional[List[str]] = None

class HighlightResponse(BaseModel):
    highlights: List[Highlight]