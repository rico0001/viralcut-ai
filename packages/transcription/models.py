from pydantic import BaseModel
from typing import List, Optional

class TranscriptSegment(BaseModel):
    start_time: float
    end_time: float
    text: str
    speaker: Optional[str] = None

class Transcript(BaseModel):
    language: str
    segments: List[TranscriptSegment]

class TranscriptionJob(BaseModel):
    job_id: str
    video_id: str
    status: str
    transcript: Optional[Transcript] = None
    error: Optional[str] = None

class TranscriptionRequest(BaseModel):
    video_id: str
    language: str
    request_id: str

class TranscriptionResponse(BaseModel):
    job_id: str
    status: str
    transcript: Optional[Transcript] = None
    error: Optional[str] = None