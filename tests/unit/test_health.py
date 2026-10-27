from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from quantflow.services.health import HealthService


def test_process_health_is_ok() -> None:
    """Process health returns an ok status."""
    result = HealthService().check_process()

    assert result.status == "ok"
    assert result.details["process"] == "ok"


def test_database_health_is_ok_with_sqlite_session() -> None:
    """Database health executes a portable lightweight query."""
    engine = create_engine("sqlite:///:memory:")
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        result = HealthService().check_database(session)

    engine.dispose()

    assert result.status == "ok"
    assert result.details["database"] == "ok"
