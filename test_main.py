from fastapi.testclient import TestClient

from main import app


def test_set_url():
    client = TestClient(app)
    response = client.post("/set", json={"url": "https://www.google.com"})
    assert response.status_code == 200


def test_get_url():
    client = TestClient(app)
    response = client.get("/10")
    print(response.json())
    assert response.status_code == 308
