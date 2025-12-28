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

"""
TEST: Verify Password Logic

1. FÖRBERED (Arrange)
   Initiera UserManager
   Sätt ett lösenord = "hemligt123"
   
   Skapa en hash av lösenordet (använd din get_password_hash funktion)
   Spara i variabeln 'hashed_pw'

2. TESTA RÄTT LÖSENORD (Assert)
   Anropa verify_password("hemligt123", hashed_pw)
   Kolla att resultatet är SANT (True)

3. TESTA FEL LÖSENORD (Assert)
   Anropa verify_password("fel123", hashed_pw)
   Kolla att resultatet är FALSKT (False)
"""

