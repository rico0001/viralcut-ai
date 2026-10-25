import pytest
from packages.agents.ranking import rank_candidates

def test_rank_candidates():
    candidates = [
        {
            "start": 0,
            "end": 10,
            "title": "Clip 1",
            "engagement_score": 75,
            "clarity": 8,
            "interest": 7,
            "story_completeness": 6,
            "information_density": 5,
        },
        {
            "start": 10,
            "end": 20,
            "title": "Clip 2",
            "engagement_score": 85,
            "clarity": 9,
            "interest": 8,
            "story_completeness": 7,
            "information_density": 6,
        },
        {
            "start": 20,
            "end": 30,
            "title": "Clip 3",
            "engagement_score": 65,
            "clarity": 7,
            "interest": 6,
            "story_completeness": 5,
            "information_density": 4,
        },
    ]

    ranked_candidates = rank_candidates(candidates)

    assert ranked_candidates[0]["title"] == "Clip 2"
    assert ranked_candidates[1]["title"] == "Clip 1"
    assert ranked_candidates[2]["title"] == "Clip 3"

def test_rank_candidates_empty():
    candidates = []
    ranked_candidates = rank_candidates(candidates)
    assert ranked_candidates == []