from pydantic import BaseSettings

class Settings(BaseSettings):
    # General settings
    APP_NAME: str = "ViralCut AI"
    APP_VERSION: str = "1.0.0"
    
    # Database settings
    DATABASE_URL: str
    DATABASE_TEST_URL: str
    
    # Redis settings
    REDIS_URL: str
    
    # AI provider settings
    AI_PROVIDER: str
    AI_API_KEY: str
    
    # Other settings
    SECRET_KEY: str
    ALLOWED_HOSTS: list[str] = []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()