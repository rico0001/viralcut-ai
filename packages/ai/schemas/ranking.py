from pydantic import BaseModel
from typing import List, Optional

class HighlightScore(BaseModel):
    start_timestamp: float
    end_timestamp: float
    score: float
    explanation: str

class ClipRanking(BaseModel):
    clip_id: str
    title: str
    highlights: List[HighlightScore]
    overall_score: float
    confidence: float
    context_warnings: Optional[List[str]] = None

class RankingResponse(BaseModel):
    clips: List[ClipRanking]
    total_clips: int
    processed_at: str