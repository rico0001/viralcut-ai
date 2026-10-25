from celery import shared_task
from packages.media.ffmpeg import render_video
from packages.media.validation import validate_rendering_inputs
from packages.shared.utils import generate_clip_filename
from services.api.db.models.clip import Clip
from services.api.db.session import get_db
from sqlalchemy.orm import Session

@shared_task(bind=True)
def render_clip(self, clip_id: int):
    db: Session = get_db()
    clip = db.query(Clip).filter(Clip.id == clip_id).first()

    if not clip:
        self.retry(exc=Exception("Clip not found"), countdown=5)

    # Validate inputs for rendering
    validation_errors = validate_rendering_inputs(clip)
    if validation_errors:
        self.retry(exc=Exception(f"Validation errors: {validation_errors}"), countdown=5)

    output_filename = generate_clip_filename(clip)
    
    try:
        # Render the video clip
        render_video(clip.source_path, output_filename, clip.editing_plan)
        clip.status = 'rendered'
        clip.output_path = output_filename
        db.commit()
    except Exception as e:
        db.rollback()
        self.retry(exc=e, countdown=5)

    return clip.output_path