from fastapi import Header, HTTPException, status
import os
from typing import Set

from src.security import settings

async def get_and_validate_key(x_api_key: str = Header(...)) -> str:
    """
    Validates the API key provided in the request header.

    Args:
        x_api_key (str): The API key extracted from the 'x-api-key' header.

    Returns:
        str: The validated API key.

    Raises:
        HTTPException: If the API key is missing or invalid (401).
    """
    if x_api_key not in settings.VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )
    return x_api_key