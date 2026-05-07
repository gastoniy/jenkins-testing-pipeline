import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the default root route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_health_route(client):
    """Test the health check route."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "UP", "message": "Application is healthy"}