import pytest

from packages.agents.qa import QualityAssuranceAgent

@pytest.fixture
def qa_agent():
    return QualityAssuranceAgent()

def test_verify_output_files_exist(qa_agent):
    output_file = "path/to/output/file.mp4"
    assert qa_agent.verify_output_file_exists(output_file) is True

def test_verify_video_duration(qa_agent):
    output_file = "path/to/output/file.mp4"
    expected_duration = 60  # seconds
    assert qa_agent.verify_video_duration(output_file, expected_duration) is True

def test_verify_audio_presence(qa_agent):
    output_file = "path/to/output/file.mp4"
    assert qa_agent.verify_audio_presence(output_file) is True

def test_check_caption_availability(qa_agent):
    caption_file = "path/to/captions.srt"
    assert qa_agent.check_caption_availability(caption_file) is True

def test_detect_blank_output(qa_agent):
    output_file = "path/to/output/file.mp4"
    assert qa_agent.detect_blank_output(output_file) is False

def test_validate_output_format(qa_agent):
    output_file = "path/to/output/file.mp4"
    expected_format = "mp4"
    assert qa_agent.validate_output_format(output_file, expected_format) is True