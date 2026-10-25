from abc import ABC, abstractmethod

class TranscriptionProvider(ABC):
    @abstractmethod
    def transcribe(self, audio_file: str) -> dict:
        """Transcribe the given audio file and return the transcript with timestamps."""
        pass

    @abstractmethod
    def detect_language(self, audio_file: str) -> str:
        """Detect the language of the given audio file."""
        pass

    @abstractmethod
    def get_transcript_segments(self, audio_file: str) -> list:
        """Return segments of the transcript with their respective timestamps."""
        pass

    @abstractmethod
    def supports_speaker_identification(self) -> bool:
        """Return True if the provider supports speaker identification, otherwise False."""
        pass