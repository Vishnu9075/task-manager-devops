from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Task Manager API"
    app_env: str = "dev"
    database_url: str = "postgresql://postgres:postgres@db:5432/tasksdb"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()