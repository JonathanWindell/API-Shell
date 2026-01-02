import pytest
from fastapi.testclient import TestClient
from main import app

from src.auth.user_manager import UserManager
from src.security.limiter import check_rate_limiter


@pytest.fixture
def client():
    """
    This function is called everytime client is used in tests.
    test/test_routes.py
    """
    return TestClient(app)


@pytest.fixture
def valid_token():
    """
    Creates fake user to simulate testing of routes.
    """
    manager = UserManager()
    return manager.create_access_token(data={"sub": "admin"})


@pytest.fixture(autouse=True)
def mock_rate_limiter():
    """
    Mocks a limiter to reply with True when check_rate_limiter is called.
    Cleans up after.
    """
    app.dependency_overrides[check_rate_limiter] = lambda: True
    yield

    app.dependency_overrides = {}
