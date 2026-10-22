from fastapi.testclient import TestClient

from app.main import base_app


def test_health() -> None:
    assert TestClient(base_app).get("/health").json()["status"] == "ok"
