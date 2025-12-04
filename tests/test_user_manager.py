import pytest
import jwt

from src.auth.user_manager import user_manager

# Test user password is hashed correctly
def test_user_password_hash():
    pwd_context = user_manager()
    secret_password = "secret123"

    hashed_password = pwd_context.get_password_hash(secret_password)

    assert secret_password != hashed_password
    assert hashed_password.startswith("$2b$")

    
# Test create user access token
def test_create_access_token():
    manager = user_manager()
    username = "testuser"

    jwt_token = manager.create_access_token(data={"sub": username})

    assert isinstance(jwt_token, str)
    assert len(jwt_token) > 0
    
    payload = jwt.decode(jwt_token, "SECRET_KEY", algorithms=["HS256"])
    assert payload["sub"] == "testuser"

