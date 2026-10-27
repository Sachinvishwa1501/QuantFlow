# QuantFlow

QuantFlow is a production-grade Python monorepo foundation for quantitative trading research in Indian equity markets.

This repository intentionally contains no trading logic, indicators, strategies, market data ingestion, broker integration, or machine learning. It provides the institutional-grade platform skeleton needed to add those modules later without changing the architecture.

## What Is Included

- Python 3.13+ package layout under `src/`
- FastAPI application factory with versioned health endpoints
- PostgreSQL support through SQLAlchemy 2.0 and Alembic
- DuckDB analytical connection factory
- Polars-ready data processing dependency
- Pydantic Settings configuration with development, staging, and production profiles
- Repository pattern base abstractions
- Structured JSON logging with request correlation support
- pytest, Ruff, Black, mypy, and pre-commit
- Dockerfile and Docker Compose for local platform services
- GitHub Actions workflow for linting, tests, type checks, Docker builds, and Alembic validation
- Documentation for setup and architecture

## Quick Start

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
copy .env.example .env
copy config\development.env.example .env.development
docker compose up -d postgres
alembic upgrade head
uvicorn quantflow.api.main:create_app --factory --reload
```

Open `http://127.0.0.1:8000/api/v1/health`.

## Repository Layout

```text
.
├── src/quantflow
│   ├── api              # FastAPI app factory, routes, dependencies
│   ├── core             # Settings, environment model, shared constants
│   ├── db               # SQLAlchemy, Alembic metadata, DuckDB support
│   ├── observability    # Structured logging
│   ├── repositories     # Repository pattern contracts and SQLAlchemy base
│   └── services         # Application services without domain trading logic
├── alembic              # Database migrations
├── docs                 # Setup and architecture guides
├── tests                # Unit tests
└── .github/workflows    # CI pipeline
```

## Development Commands

```powershell
ruff check .
black --check .
mypy src
pytest
docker compose up --build
```

## Design Boundaries

QuantFlow currently stops at platform foundation concerns:

- Application lifecycle
- Configuration
- Database connectivity
- Migration framework
- Repository pattern
- Observability
- Health checks
- Developer tooling

Future modules such as market data, screening, backtesting, risk management, execution, and analytics should be added under clear package boundaries without changing these foundations.

See [docs/setup.md](docs/setup.md) and [docs/architecture.md](docs/architecture.md).
