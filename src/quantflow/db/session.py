from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from quantflow.core.settings import get_settings

settings = get_settings()

engine = create_engine(
    settings.postgres_dsn,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)
