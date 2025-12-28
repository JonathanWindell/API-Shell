from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

# Create hashed password using bcrypt
class user_manager:
    # Constants for user token
    SECRET_KEY = "SECRET_KEY"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Create hashing rules for password 
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    # Get the password hash
    def get_password_hash(self, password):
        hashed_password = self.pwd_context.hash(password)

        return hashed_password

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(self.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt
    

"""
METOD verify_password(self, plain_password, hashed_password):
        
        # Använd ditt verktyg (pwd_context)
        # Funktionen heter ofta .verify(klart_lösenord, hash) i biblioteket
        
        RETURNERA resultatet (som blir True eller False)
"""