from typing import List, Dict, Any
from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    audio_file_path: str
    language: str = "en"

class TranscriptionResponse(BaseModel):
    transcript: str
    segments: List[Dict[str, Any]]

class TranscriptionAgent:
    def __init__(self, provider):
        self.provider = provider

    def transcribe(self, request: TranscriptionRequest) -> TranscriptionResponse:
        audio_file_path = request.audio_file_path
        language = request.language
        
        # Call the provider's transcription method
        transcript, segments = self.provider.transcribe(audio_file_path, language)
        
        return TranscriptionResponse(transcript=transcript, segments=segments)