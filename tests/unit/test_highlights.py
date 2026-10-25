import pytest
from packages.agents.highlight_detection import HighlightDetectionAgent

@pytest.fixture
def highlight_detection_agent():
    return HighlightDetectionAgent()

def test_highlight_detection_with_valid_input(highlight_detection_agent):
    # Mock input data
    transcript = "This is a sample transcript with engaging moments."
    timestamps = [(0, 5), (5, 10), (10, 15)]
    
    # Call the highlight detection method
    highlights = highlight_detection_agent.detect_highlights(transcript, timestamps)
    
    # Assert that highlights are detected correctly
    assert isinstance(highlights, list)
    assert len(highlights) > 0

def test_highlight_detection_with_empty_transcript(highlight_detection_agent):
    # Mock input data
    transcript = ""
    timestamps = [(0, 5), (5, 10)]
    
    # Call the highlight detection method
    highlights = highlight_detection_agent.detect_highlights(transcript, timestamps)
    
    # Assert that no highlights are detected
    assert highlights == []

def test_highlight_detection_with_no_timestamps(highlight_detection_agent):
    # Mock input data
    transcript = "This is a sample transcript."
    timestamps = []
    
    # Call the highlight detection method
    highlights = highlight_detection_agent.detect_highlights(transcript, timestamps)
    
    # Assert that no highlights are detected
    assert highlights == []

def test_highlight_detection_with_invalid_timestamps(highlight_detection_agent):
    # Mock input data
    transcript = "This is a sample transcript."
    timestamps = [(10, 5)]  # Invalid timestamp
    
    # Call the highlight detection method
    highlights = highlight_detection_agent.detect_highlights(transcript, timestamps)
    
    # Assert that no highlights are detected
    assert highlights == []