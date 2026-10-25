from celery import shared_task
from packages.transcription.provider import TranscriptionProvider
from packages.media.audio import extract_audio
from packages.shared.utils import log_error

@shared_task(bind=True)
def transcribe_video(self, video_path: str, provider: str) -> dict:
    try:
        # Extract audio from the video
        audio_path = extract_audio(video_path)
        
        # Initialize the transcription provider
        transcription_provider = TranscriptionProvider(provider)
        
        # Perform transcription
        transcript = transcription_provider.transcribe(audio_path)
        
        return {
            "status": "success",
            "transcript": transcript
        }
    except Exception as e:
        log_error(f"Transcription failed for {video_path}: {str(e)}")
        self.retry(exc=e, countdown=60)  # Retry after 60 seconds
        return {
            "status": "failed",
            "error": str(e)
        }