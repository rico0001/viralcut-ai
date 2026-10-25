import pytest
from packages.media.validation import validate_timestamps

def test_valid_timestamps():
    # Test with valid timestamps
    assert validate_timestamps(0, 10, 20) == True
    assert validate_timestamps(5, 15, 25) == True

def test_invalid_timestamps():
    # Test with invalid timestamps
    assert validate_timestamps(10, 5, 20) == False  # Start > End
    assert validate_timestamps(0, 10, 5) == False   # End < Clip Duration
    assert validate_timestamps(-1, 10, 20) == False  # Negative start
    assert validate_timestamps(0, 10, -5) == False   # Negative end
    assert validate_timestamps(0, 10, 10) == False   # End equals duration

def test_edge_case_timestamps():
    # Test edge cases
    assert validate_timestamps(0, 0, 0) == True       # All zero
    assert validate_timestamps(0, 1, 1) == True       # Minimal valid case
    assert validate_timestamps(0, 1, 2) == True       # Valid case with duration greater than end
    assert validate_timestamps(1, 2, 2) == False      # Start equals end
    assert validate_timestamps(1, 2, 1) == False      # Start > duration