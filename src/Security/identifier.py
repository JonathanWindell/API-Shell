# Dependencies import
from fastapi import Header, HTTPException, status
import os
from typing import Set

# File import
from settings import VALID_API_KEY

# Get and validate keys. Simplifies process given all users must have key.
async def get_and_validate_key(x_api_key: str = Header(...)) -> str:
    if x_api_key not in VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detaiL="Invalid or missing API Key"
        )
    return x_api_key