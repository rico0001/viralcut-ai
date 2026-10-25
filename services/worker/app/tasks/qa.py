from celery import shared_task
from packages.media.validation import validate_video
from packages.media.ffmpeg import check_video_quality
from packages.shared.utils import log_error

@shared_task(bind=True)
def qa_task(self, video_path):
    try:
        # Validate the video file
        validation_result = validate_video(video_path)
        if not validation_result['is_valid']:
            raise ValueError(f"Video validation failed: {validation_result['error']}")

        # Check the quality of the video
        quality_result = check_video_quality(video_path)
        if not quality_result['is_quality_ok']:
            raise ValueError(f"Video quality check failed: {quality_result['error']}")

        return {
            'status': 'success',
            'message': 'Video passed quality assurance checks.'
        }

    except Exception as e:
        log_error(f"Quality assurance task failed: {str(e)}")
        self.retry(exc=e)