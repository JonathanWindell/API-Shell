import pytest
import jwt

from src.auth.user_manager import UserManager

def test_user_password_hash():
    """
    Verifies that the password is correctly hashed and formatted (Bcrypt).
    """
    # Arrange
    manager = UserManager()
    secret_password = "secret123"

    # Act
    hashed_password = manager.get_password_hash(secret_password)

    # Assert
    assert secret_password != hashed_password
    assert hashed_password.startswith("$2b$")

def test_create_access_token():
    """
    Verifies that the token is created, is a string, and contains the correct payload.
    """
    # Arrange
    manager = UserManager()
    username = "testuser"

    # Act
    jwt_token = manager.create_access_token(data={"sub": username})

    # Assert
    assert isinstance(jwt_token, str)
    assert len(jwt_token) > 0
    
    # Check payload
    payload = jwt.decode(jwt_token, manager.SECRET_KEY, algorithms=[manager.ALGORITHM])
    assert payload["sub"] == "testuser"

def test_verify_user_password():
    """
    Verifies that the password verification logic works for both correct and incorrect passwords.
    """
    # Arrange
    manager = UserManager()
    password = "Secret123"

    # Act
    hashed_password = manager.get_password_hash(password)

    # Assert
    assert manager.verify_password("Secret123", hashed_password) == True
    assert manager.verify_password("NotSecret123", hashed_password) == False


