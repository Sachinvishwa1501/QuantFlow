# QuantFlow Setup Guide

## Prerequisites

- Python 3.13+
- Docker Desktop or compatible Docker runtime
- PostgreSQL client tools are optional but useful

## Local Development

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
copy .env.example .env
docker compose up -d postgres
alembic upgrade head
uvicorn quantflow.api.main:create_app --factory --reload
```

## Configuration Layers

QuantFlow uses Pydantic Settings with the `QUANTFLOW_` environment prefix. At runtime it loads `.env` and then `.env.<environment>` when that file exists. Real environment variables supplied by the shell, container runtime, or deployment platform override file values.

| Environment | `QUANTFLOW_ENV` | Behavior |
| --- | --- | --- |
| Development | `development` | API docs enabled, local defaults allowed |
| Staging | `staging` | Debug disabled, production-like runtime |
| Production | `production` | Debug disabled, API docs disabled |

Use `.env` for local development only. Staging and production should inject environment variables through the deployment platform or secret manager.

Checked-in templates live in `config/`:

- `config/development.env.example`
- `config/staging.env.example`
- `config/production.env.example`

## Database Migrations

Create a migration:

```powershell
alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```powershell
alembic upgrade head
```

## Quality Gates

```powershell
ruff check .
black --check .
mypy src
pytest
pre-commit run --all-files
```

## Docker

```powershell
docker compose up --build
```

The API is exposed on `http://127.0.0.1:8000`.
