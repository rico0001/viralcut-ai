from typing import List, Dict, Any

class ClipSelectionAgent:
    def __init__(self, clips: List[Dict[str, Any]], diversity_constraints: int = 3):
        self.clips = clips
        self.diversity_constraints = diversity_constraints

    def select_clips(self) -> List[Dict[str, Any]]:
        selected_clips = self.rank_and_filter_clips()
        return self.ensure_diversity(selected_clips)

    def rank_and_filter_clips(self) -> List[Dict[str, Any]]:
        # Sort clips based on their engagement score
        sorted_clips = sorted(self.clips, key=lambda x: x['engagement_score'], reverse=True)
        return sorted_clips[:self.diversity_constraints]

    def ensure_diversity(self, selected_clips: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        unique_topics = set()
        diverse_clips = []

        for clip in selected_clips:
            if clip['topic'] not in unique_topics:
                unique_topics.add(clip['topic'])
                diverse_clips.append(clip)

        return diverse_clips[:self.diversity_constraints]  # Return up to the diversity constraint limit

    def get_selected_clips(self) -> List[Dict[str, Any]]:
        return self.select_clips()