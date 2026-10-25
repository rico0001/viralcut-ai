# Constants for the ViralCut AI application

# Video processing constants
VIDEO_MAX_DURATION = 3600  # Maximum video duration in seconds (1 hour)
VIDEO_MIN_DURATION = 5      # Minimum video duration in seconds
VIDEO_MAX_SIZE_MB = 500     # Maximum video file size in megabytes

# Transcription constants
TRANSCRIPTION_LANGUAGE = 'en'  # Default language for transcription
TRANSCRIPTION_TIMEOUT = 300      # Timeout for transcription requests in seconds

# Clip generation constants
CLIP_MIN_DURATION = 15  # Minimum duration for generated clips in seconds
CLIP_MAX_DURATION = 60  # Maximum duration for generated clips in seconds
CLIP_DEFAULT_COUNT = 5  # Default number of clips to generate

# Captioning constants
CAPTION_MAX_LENGTH = 42  # Maximum characters per caption line
CAPTION_MIN_DURATION = 1  # Minimum duration for captions to display in seconds

# Metadata constants
DEFAULT_TITLE = "Generated Clip"  # Default title for generated clips
DEFAULT_DESCRIPTION = "This is a generated clip from a longer video."  # Default description
DEFAULT_HASHTAGS = ["#ViralCutAI", "#Shorts", "#Highlights"]  # Default hashtags for clips

# Error messages
ERROR_INVALID_VIDEO = "The provided video is invalid or unsupported."
ERROR_TRANSCRIPTION_FAILED = "Transcription failed. Please try again."
ERROR_CLIP_GENERATION_FAILED = "Clip generation failed. Please check the logs."