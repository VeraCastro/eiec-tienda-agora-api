import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.smoke
def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.api
def test_version_returns_name_and_version():
    response = client.get("/version")
    body = response.json()

    assert response.status_code == 200
    assert body["name"] == "Tienda Agora API"
    assert "version" in body
