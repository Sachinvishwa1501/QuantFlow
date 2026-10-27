from typing import Literal

from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.orm import Session

from quantflow import __version__


class HealthCheckResult(BaseModel):
    """Serializable result for health-check endpoints."""

    status: Literal["ok", "degraded"]
    service: str = "quantflow"
    version: str = __version__
    details: dict[str, str] = Field(default_factory=dict)


class HealthService:
    """Service responsible for application health checks."""

    def check_process(self) -> HealthCheckResult:
        """Return an in-process liveness result."""
        return HealthCheckResult(status="ok", details={"process": "ok"})

    def check_database(self, session: Session) -> HealthCheckResult:
        """Return database readiness status.

        Args:
            session: SQLAlchemy session used to execute a lightweight readiness query.

        Returns:
            A readiness result indicating whether PostgreSQL can execute a query.
        """
        try:
            session.execute(text("SELECT 1"))
        except Exception as exc:
            return HealthCheckResult(status="degraded", details={"database": str(exc)})
        return HealthCheckResult(status="ok", details={"database": "ok"})
