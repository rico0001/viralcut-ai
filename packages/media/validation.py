from pydantic import BaseModel, validator
from typing import List, Optional

class MediaFileValidation(BaseModel):
    file_path: str
    file_size: int
    duration: float
    codec: str
    audio_present: bool

    @validator('file_path')
    def validate_file_path(cls, v):
        if not v.endswith(('.mp4', '.mkv', '.avi', '.mov')):
            raise ValueError('Invalid file type. Supported formats are: .mp4, .mkv, .avi, .mov')
        return v

    @validator('file_size')
    def validate_file_size(cls, v):
        if v <= 0:
            raise ValueError('File size must be greater than 0')
        return v

    @validator('duration')
    def validate_duration(cls, v):
        if v <= 0:
            raise ValueError('Duration must be greater than 0')
        return v

    @validator('codec')
    def validate_codec(cls, v):
        if v not in ['h264', 'hevc', 'vp9']:
            raise ValueError('Unsupported codec. Supported codecs are: h264, hevc, vp9')
        return v

    @validator('audio_present')
    def validate_audio_present(cls, v):
        if not v:
            raise ValueError('Audio must be present in the media file')
        return v

def validate_media_file(media_file: MediaFileValidation) -> List[str]:
    errors = []
    try:
        media_file.validate()
    except ValueError as e:
        errors.append(str(e))
    return errors