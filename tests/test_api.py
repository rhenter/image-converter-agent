from fastapi.testclient import TestClient

from src.main import base_app


def test_health() -> None:
    assert TestClient(base_app).get("/health").json()["status"] == "ok"
