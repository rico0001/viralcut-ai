from typing import Dict, Any

class ProgressTracker:
    def __init__(self):
        self.progress: Dict[str, Any] = {}

    def start_task(self, task_id: str):
        self.progress[task_id] = {
            "status": "pending",
            "details": {},
        }

    def update_task(self, task_id: str, status: str, details: Dict[str, Any] = None):
        if task_id in self.progress:
            self.progress[task_id]["status"] = status
            if details is not None:
                self.progress[task_id]["details"].update(details)

    def complete_task(self, task_id: str):
        self.update_task(task_id, "completed")

    def fail_task(self, task_id: str, error_message: str):
        self.update_task(task_id, "failed", {"error": error_message})

    def get_progress(self, task_id: str) -> Dict[str, Any]:
        return self.progress.get(task_id, None)

    def get_all_progress(self) -> Dict[str, Any]:
        return self.progress