import pytest
from packages.media.audio import AudioProcessor

def test_audio_extraction():
    audio_processor = AudioProcessor()
    video_file = "tests/media/sample_video.mp4"  # Replace with an actual test video file
    extracted_audio = audio_processor.extract_audio(video_file)
    
    assert extracted_audio is not None
    assert extracted_audio.endswith(".wav")  # Assuming the output is in WAV format

def test_audio_normalization():
    audio_processor = AudioProcessor()
    audio_file = "tests/media/sample_audio.wav"  # Replace with an actual test audio file
    normalized_audio = audio_processor.normalize_audio(audio_file)
    
    assert normalized_audio is not None
    assert normalized_audio == audio_file  # Replace with expected normalized output

def test_audio_format_conversion():
    audio_processor = AudioProcessor()
    input_audio = "tests/media/sample_audio.wav"  # Replace with an actual test audio file
    output_audio = audio_processor.convert_audio_format(input_audio, "mp3")
    
    assert output_audio is not None
    assert output_audio.endswith(".mp3")  # Check if the output is in MP3 format

def test_invalid_audio_file():
    audio_processor = AudioProcessor()
    invalid_audio_file = "tests/media/invalid_audio.txt"  # Invalid file type
    
    with pytest.raises(ValueError):
        audio_processor.extract_audio(invalid_audio_file)