class MockAIProvider:
    def transcribe(self, audio_file):
        return {
            "transcript": "This is a mock transcription.",
            "timestamps": [
                {"start": 0, "end": 5, "text": "This is a mock"},
                {"start": 5, "end": 10, "text": "transcription."}
            ]
        }

    def analyze_content(self, transcript):
        return {
            "highlights": [
                {"start": 0, "end": 5, "importance": 0.9, "text": "This is a mock"},
                {"start": 5, "end": 10, "importance": 0.8, "text": "transcription."}
            ]
        }

    def generate_metadata(self, highlights):
        return {
            "titles": ["Mock Title 1", "Mock Title 2"],
            "descriptions": ["This is a mock description."],
            "hashtags": ["#mock", "#test"]
        }