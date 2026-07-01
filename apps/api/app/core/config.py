import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Settings class using pydantic-settings to validate environment variables.
    Can load from active env or custom env files.
    """
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # Database
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "cybernest"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/cybernest"

    # JWT & Crypto
    JWT_SECRET_KEY: str = "dev_secret_key_extremely_insecure_please_change"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    AGENT_AUTH_TOKEN: str = "dev_agent_token_secret"

    # Config loading order: env files followed by system env.
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 
            ".env.development"
        ) if os.path.exists(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 
            ".env.development"
        )) else ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
