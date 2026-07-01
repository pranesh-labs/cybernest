import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class AgentSettings(BaseSettings):
    """
    Settings loader for the fingerprinting agent daemon.
    """
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # Identity
    AGENT_ID: str = "agent-default-1"

    # API Connection
    API_URL: str = "http://localhost:8000/api/v1"
    AGENT_AUTH_TOKEN: str = "dev_agent_token_secret"

    # Scheduler Settings
    HEARTBEAT_INTERVAL_SECONDS: int = 30
    SCAN_INTERVAL_SECONDS: int = 300

    # Config loading
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
            ".env.development"
        ) if os.path.exists(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
            ".env.development"
        )) else ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

agent_settings = AgentSettings()
