from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from quantflow.api.dependencies import get_db_session
from quantflow.services.health import HealthCheckResult, HealthService

router = APIRouter()
DB_SESSION_DEPENDENCY = Depends(get_db_session)
HEALTH_SERVICE_DEPENDENCY = Depends(HealthService)


@router.get("/health", response_model=HealthCheckResult)
def health() -> HealthCheckResult:
    """Return a lightweight process health check."""
    return HealthService().check_process()


@router.get("/health/ready", response_model=HealthCheckResult)
def readiness(
    session: Session = DB_SESSION_DEPENDENCY,
    service: HealthService = HEALTH_SERVICE_DEPENDENCY,
) -> HealthCheckResult:
    """Return readiness for dependencies required to serve traffic."""
    return service.check_database(session)
