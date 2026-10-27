from fastapi.testclient import TestClient

from quantflow.api.main import create_app
from quantflow.core.environment import Environment
from quantflow.core.settings import Settings


def test_health_endpoint() -> None:
    """The liveness endpoint returns platform health."""
    app = create_app(Settings(env=Environment.DEVELOPMENT))
    client = TestClient(app)

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
