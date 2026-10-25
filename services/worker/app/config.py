from pydantic import BaseSettings

class Settings(BaseSettings):
    # Celery configuration
    broker_url: str = "redis://localhost:6379/0"
    result_backend: str = "redis://localhost:6379/0"
    task_serializer: str = "json"
    result_serializer: str = "json"
    accept_content: list = ["json"]
    timezone: str = "UTC"
    enable_utc: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"