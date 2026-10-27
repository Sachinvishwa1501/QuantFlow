from collections.abc import Generator

from sqlalchemy.orm import Session

from quantflow.db.session import SessionLocal


def get_db_session() -> Generator[Session]:
    """Yield a SQLAlchemy session for request-scoped database access."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
