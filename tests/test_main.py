from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

c = 1000

f = 55

bb = 999


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
