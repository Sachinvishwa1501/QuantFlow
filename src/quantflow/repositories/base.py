from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

ModelT = TypeVar("ModelT")


class Repository[ModelT](ABC):
    """Protocol-like base class for repository implementations."""

    @abstractmethod
    def get(self, entity_id: UUID) -> ModelT | None:
        """Return one entity by identifier."""

    @abstractmethod
    def list(self, limit: int = 100, offset: int = 0) -> Sequence[ModelT]:
        """Return a paginated sequence of entities."""


class SqlAlchemyRepository[ModelT](Repository[ModelT]):
    """Base SQLAlchemy repository for ORM-backed entities."""

    model: type[ModelT]

    def __init__(self, session: Session) -> None:
        """Initialize the repository with a database session."""
        self.session = session

    def get(self, entity_id: UUID) -> ModelT | None:
        """Return one entity by primary key."""
        return self.session.get(self.model, entity_id)

    def list(self, limit: int = 100, offset: int = 0) -> Sequence[ModelT]:
        """Return a paginated list of entities."""
        statement = self.session.query(self.model).limit(limit).offset(offset)
        return statement.all()
