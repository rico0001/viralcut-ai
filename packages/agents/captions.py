from typing import List, Dict

class CaptionAgent:
    def __init__(self, caption_style: str = "default"):
        self.caption_style = caption_style

    def generate_captions(self, transcript: List[Dict[str, str]]) -> List[str]:
        captions = []
        for segment in transcript:
            start_time = segment['start']
            end_time = segment['end']
            text = segment['text']
            caption = self.format_caption(start_time, end_time, text)
            captions.append(caption)
        return captions

    def format_caption(self, start: str, end: str, text: str) -> str:
        return f"[{start} --> {end}] {text}"

    def emphasize_keywords(self, text: str, keywords: List[str]) -> str:
        for keyword in keywords:
            text = text.replace(keyword, f"**{keyword}**")
        return text

    def validate_captions(self, captions: List[str]) -> bool:
        for caption in captions:
            if not self.is_caption_valid(caption):
                return False
        return True

    def is_caption_valid(self, caption: str) -> bool:
        # Implement validation logic (e.g., length, formatting)
        return True

    def set_caption_style(self, style: str):
        self.caption_style = style

    def get_caption_style(self) -> str:
        return self.caption_style