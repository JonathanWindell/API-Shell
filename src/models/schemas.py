from pydantic import BaseModel


# Defines the response schema for the token
class Token(BaseModel):
    access_token: str
    token_type: str


# Defines the response schema for user data
class UserResponse(BaseModel):
    username: str
    message: str
