import pytest

def test_user_password_hash():
    pwd_context = UserManager()
    secret_password = "secret123"

    hashed_password = pwd_context.get_password_hash(secret_password)

    assert password != hashed_password
    assert hashed_password.startswith("$2b$")

    
    