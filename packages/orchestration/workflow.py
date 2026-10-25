from typing import Any, Dict, List

class WorkflowOrchestrator:
    def __init__(self):
        self.state = {}
        self.jobs = []

    def add_job(self, job: Dict[str, Any]) -> None:
        self.jobs.append(job)
        self.state[job['id']] = 'pending'

    def start_job(self, job_id: str) -> None:
        if job_id in self.state:
            self.state[job_id] = 'running'

    def complete_job(self, job_id: str) -> None:
        if job_id in self.state:
            self.state[job_id] = 'completed'

    def fail_job(self, job_id: str) -> None:
        if job_id in self.state:
            self.state[job_id] = 'failed'

    def get_job_status(self, job_id: str) -> str:
        return self.state.get(job_id, 'not found')

    def get_all_jobs(self) -> List[Dict[str, Any]]:
        return self.jobs

    def reset(self) -> None:
        self.state.clear()
        self.jobs.clear()