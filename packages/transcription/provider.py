from abc import ABC, abstractmethod

class TranscriptionProvider(ABC):
    @abstractmethod
    def transcribe(self, audio_file: str) -> dict:
        pass

    @abstractmethod
    def get_transcription_status(self, transcription_id: str) -> dict:
        pass

    @abstractmethod
    def cancel_transcription(self, transcription_id: str) -> bool:
        pass

    @abstractmethod
    def get_supported_languages(self) -> list:
        pass