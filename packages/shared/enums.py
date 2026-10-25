from enum import Enum

class VideoProcessingStatus(Enum):
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class ClipFormat(Enum):
    MP4 = "mp4"
    AVI = "avi"
    MOV = "mov"

class CaptionStyle(Enum):
    DEFAULT = "default"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"