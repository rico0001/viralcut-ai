from typing import List, Dict, Any
import whisper

class WhisperTranscriptionProvider:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file: str) -> Dict[str, Any]:
        result = self.model.transcribe(audio_file)
        return {
            "text": result["text"],
            "segments": self._format_segments(result["segments"]),
            "language": result["language"]
        }

    def _format_segments(self, segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        formatted_segments = []
        for segment in segments:
            formatted_segments.append({
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })
        return formatted_segments