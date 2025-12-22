# Dependencies import
from fastapi import Header, HTTPException, status
import os
from typing import Set

# File import
from src.security import settings

# Get and validate keys. Simplifies process given all users must have key.
async def get_and_validate_key(x_api_key: str = Header(...)) -> str:
    if x_api_key not in settings.VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )
    return x_api_key