from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

c = 100

f = 55
gg = 444
a = 14


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
