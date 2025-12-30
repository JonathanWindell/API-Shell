from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

class UserManager:
    """
    Handles user security operations including password hashing 
    and JWT token generation.
    """
    
    # TODO: In production, fetch these from environment variables (.env) to be secure!
    SECRET_KEY = "SECRET_KEY"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get_password_hash(self, password: str) -> str:
        """
        Takes a plain text password and returns a hashed string using Bcrypt.
        """
        hashed_password = self.pwd_context.hash(password)

        return hashed_password
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies a plain text password against the stored hash.
        Returns True if they match, False otherwise.
        """
        result = self.pwd_context.verify(plain_password, hashed_password)

        return result

    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str:
        """
        Generates a JWT token containing user data.
        
        Args:
            data (dict): The payload to encode (e.g., {"sub": "username"}).
            expires_delta (timedelta, optional): Custom expiration time. 
                                                 Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.
        
        Returns:
            str: The encoded JWT token as a string.
        """
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes = self.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt
    

