from celery import shared_task
from packages.ai.schemas.highlight import HighlightSchema
from packages.agents.highlight_detection import HighlightDetectionAgent
from packages.orchestration.workflow import WorkflowOrchestrator

@shared_task(bind=True)
def detect_highlights(self, project_id, video_metadata, transcript):
    orchestrator = WorkflowOrchestrator()
    agent = HighlightDetectionAgent()

    try:
        # Step 1: Analyze the transcript and video metadata to find highlights
        highlights = agent.detect_highlights(video_metadata, transcript)

        # Step 2: Validate and format the highlights
        formatted_highlights = [HighlightSchema(**highlight) for highlight in highlights]

        # Step 3: Persist the highlights in the database
        orchestrator.save_highlights(project_id, formatted_highlights)

        return formatted_highlights

    except Exception as e:
        self.retry(exc=e, countdown=60)  # Retry the task in case of failure
        return None