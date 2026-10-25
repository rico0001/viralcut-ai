import pytest
from packages.media.validation import validate_source

def test_validate_supported_video_format():
    assert validate_source("video.mp4") == True
    assert validate_source("video.mov") == True
    assert validate_source("video.avi") == True

def test_validate_unsupported_video_format():
    assert validate_source("video.txt") == False
    assert validate_source("video.docx") == False
    assert validate_source("video.mp3") == False

def test_validate_file_size():
    # Assuming validate_source also checks file size
    assert validate_source("large_video.mp4", max_size=100 * 1024 * 1024) == False  # 100 MB limit
    assert validate_source("small_video.mp4", max_size=100 * 1024 * 1024) == True

def test_validate_duration():
    # Assuming validate_source checks duration
    assert validate_source("short_video.mp4", min_duration=5) == True  # Minimum 5 seconds
    assert validate_source("too_short.mp4", min_duration=5) == False

def test_validate_audio_presence():
    # Assuming validate_source checks for audio presence
    assert validate_source("video_with_audio.mp4") == True
    assert validate_source("video_without_audio.mp4") == False

def test_validate_invalid_file():
    assert validate_source("invalid_file.xyz") == False
    assert validate_source("corrupted_video.mp4") == False  # Assuming this file is corrupted