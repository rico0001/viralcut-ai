import pytest
from packages.agents.captions import CaptionAgent

@pytest.fixture
def caption_agent():
    return CaptionAgent()

def test_generate_captions(caption_agent):
    transcript = [
        {"start": 0, "end": 2, "text": "Hello, welcome to the video."},
        {"start": 2, "end": 5, "text": "Today we will discuss AI."},
        {"start": 5, "end": 8, "text": "Let's get started!"}
    ]
    expected_captions = [
        {"start": 0, "end": 2, "text": "Hello, welcome to the video."},
        {"start": 2, "end": 5, "text": "Today we will discuss AI."},
        {"start": 5, "end": 8, "text": "Let's get started!"}
    ]
    generated_captions = caption_agent.generate_captions(transcript)
    assert generated_captions == expected_captions

def test_caption_formatting(caption_agent):
    captions = [
        {"start": 0, "end": 2, "text": "Hello, welcome to the video."},
        {"start": 2, "end": 5, "text": "Today we will discuss AI."}
    ]
    formatted_captions = caption_agent.format_captions(captions)
    assert all(isinstance(caption['text'], str) for caption in formatted_captions)
    assert len(formatted_captions) == len(captions)

def test_caption_timing(caption_agent):
    captions = [
        {"start": 0, "end": 2, "text": "Hello."},
        {"start": 2, "end": 5, "text": "Welcome!"}
    ]
    assert caption_agent.validate_timing(captions) is True

    invalid_captions = [
        {"start": 0, "end": 2, "text": "Hello."},
        {"start": 1, "end": 5, "text": "Welcome!"}  # Overlapping timing
    ]
    assert caption_agent.validate_timing(invalid_captions) is False