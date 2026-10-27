# QuantFlow Architecture Guide

## Purpose

QuantFlow is structured as a long-lived research platform for Indian equity markets. The current repository establishes platform foundations only. Trading and research capabilities must be added as separate modules with clear boundaries.

## Layers

```text
API layer
  FastAPI routes, request validation, response models

Service layer
  Application use cases and orchestration

Repository layer
  Database access through persistence abstractions

Database layer
  SQLAlchemy sessions, ORM metadata, Alembic migrations, DuckDB connections

Core layer
  Settings, environment model, shared platform primitives
```

## Package Responsibilities

| Package | Responsibility |
| --- | --- |
| `quantflow.api` | HTTP app construction, routes, dependencies |
| `quantflow.core` | Environment-aware configuration |
| `quantflow.db` | Relational and analytical database connectivity |
| `quantflow.repositories` | Persistence access contracts and base implementations |
| `quantflow.services` | Application services independent of HTTP details |
| `quantflow.observability` | Structured logging and future tracing hooks |

## Future Modules

Add future capabilities as new packages under `src/quantflow`, for example:

- `market_data`
- `screening`
- `backtesting`
- `risk`
- `execution`
- `analytics`

Each module should expose services and repositories through its own package and avoid coupling directly to unrelated modules. Cross-module work should happen through explicit service interfaces or application-level orchestration.

## Database Strategy

PostgreSQL is the system-of-record database for transactional platform state. SQLAlchemy models should inherit from `quantflow.db.base.Base`, and schema changes must go through Alembic migrations.

DuckDB is reserved for analytical workloads and local research datasets. It should not become the source of truth for platform metadata.

## Configuration Strategy

Configuration is layered by environment:

1. Code defaults for safe local development
2. `.env` file for developer workstations
3. Environment variables for staging and production
4. Deployment secret stores for credentials

Production disables debug mode and API documentation automatically.

## Non-Goals In This Foundation

The foundation intentionally excludes:

- Trading signals
- Technical indicators
- Strategies
- Broker adapters
- Market data ingestion
- Machine learning
- Execution routing
- Portfolio optimization

Those concerns can be added later without replacing the platform skeleton.
