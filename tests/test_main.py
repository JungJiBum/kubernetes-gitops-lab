from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Kubernetes GitOps Lab"
    assert "environment" in data
    assert "version" in data


def test_health_live():
    response = client.get("/health/live")
    assert response.status_code == 200


def test_health_ready():
    response = client.get("/health/ready")
    assert response.status_code == 200


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()