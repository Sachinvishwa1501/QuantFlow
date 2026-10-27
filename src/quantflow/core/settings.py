from __future__ import annotations

from functools import lru_cache
from os import getenv
from pathlib import Path

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from quantflow.core.environment import Environment


class Settings(BaseSettings):
    """Application settings loaded from environment variables and `.env` files."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="QUANTFLOW_",
        case_sensitive=False,
        extra="ignore",
    )

    env: Environment = Environment.DEVELOPMENT
    app_name: str = "QuantFlow"
    debug: bool = False
    enable_docs: bool = True
    log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    postgres_dsn: str = "postgresql+psycopg://quantflow:quantflow@localhost:5432/quantflow"
    duckdb_path: Path = Field(default=Path("./data/quantflow.duckdb"))

    @model_validator(mode="after")
    def apply_environment_defaults(self) -> Settings:
        """Apply conservative defaults for staging and production environments."""
        if self.env is Environment.DEVELOPMENT:
            self.debug = self.debug or False
            self.enable_docs = True

        if self.env in {Environment.STAGING, Environment.PRODUCTION}:
            self.debug = False

        if self.env is Environment.PRODUCTION:
            self.enable_docs = False

        return self


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings with layered environment files."""
    env_name = getenv("QUANTFLOW_ENV", Environment.DEVELOPMENT.value)
    return Settings(_env_file=(".env", f".env.{env_name}"))
