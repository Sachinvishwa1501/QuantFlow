from __future__ import annotations

import uvicorn
from fastapi import FastAPI

from quantflow.api.routes import health
from quantflow.core.settings import Settings, get_settings
from quantflow.observability.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure the QuantFlow FastAPI application."""
    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings)

    app = FastAPI(
        title=resolved_settings.app_name,
        version="0.1.0",
        docs_url="/docs" if resolved_settings.enable_docs else None,
        redoc_url="/redoc" if resolved_settings.enable_docs else None,
        openapi_url="/openapi.json" if resolved_settings.enable_docs else None,
    )
    app.include_router(health.router, prefix="/api/v1", tags=["health"])
    return app


def run() -> None:
    """Run the API server using settings from the active environment."""
    settings = get_settings()
    uvicorn.run(
        "quantflow.api.main:create_app",
        factory=True,
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )
