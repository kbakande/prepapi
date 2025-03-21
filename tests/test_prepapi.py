#  test prepapi app
from fastapi.testclient import TestClient
from prepapi.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_greet():
    response = client.get("/greet/Erik")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Erik!"}