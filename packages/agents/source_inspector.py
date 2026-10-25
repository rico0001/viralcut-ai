from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any
import ffprobe

class SourceReport(BaseModel):
    valid: bool
    message: str
    metadata: Optional[Dict[str, Any]] = None

class SourceInspector:
    def __init__(self, allowed_formats: set, max_duration: int, max_size: int):
        self.allowed_formats = allowed_formats
        self.max_duration = max_duration
        self.max_size = max_size

    def validate_source(self, source: str) -> SourceReport:
        if not self.is_accessible(source):
            return SourceReport(valid=False, message="Source is not accessible.")
        
        metadata = self.get_media_metadata(source)
        if not metadata:
            return SourceReport(valid=False, message="Failed to extract metadata.")
        
        if metadata['duration'] > self.max_duration:
            return SourceReport(valid=False, message="Video exceeds maximum duration.")
        
        if metadata['size'] > self.max_size:
            return SourceReport(valid=False, message="Video exceeds maximum size.")
        
        if metadata['format'] not in self.allowed_formats:
            return SourceReport(valid=False, message="Unsupported video format.")
        
        return SourceReport(valid=True, message="Source is valid.", metadata=metadata)

    def is_accessible(self, source: str) -> bool:
        # Implement accessibility check logic (e.g., check URL, file path)
        return True

    def get_media_metadata(self, source: str) -> Optional[Dict[str, Any]]:
        try:
            metadata = ffprobe.FFProbe(source)
            return {
                'duration': metadata.duration,
                'size': metadata.size,
                'format': metadata.format_name,
            }
        except Exception as e:
            return None