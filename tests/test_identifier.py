import pytest
from fastapi import HTTPException
from src.security.identifier import get_and_validate_key
from src.security import settings 

# test valid key
@pytest.mark.asyncio
async def test_valid_api_key():
    """
    Verifies that valid API keys are correctly validated.
    """
    # Arrange
    settings.VALID_API_KEYS = {"Test_Api_Key"}

    # Act
    result = await get_and_validate_key("Test_Api_Key")

    # Assert
    assert result == "Test_Api_Key"

# test invalid key
@pytest.mark.asyncio
async def test_invalid_api_key():
    """
    Verifies that invalid API keys raise an HTTPException.
    """
    # Arrange
    settings.VALID_API_KEYS = {"Test_Api_Key"}

    # Act
    with pytest.raises(HTTPException) as exec_info:
        await get_and_validate_key("Wrong_Api_Key")

    # Assert
    assert exec_info.value.status_code == 401
    assert exec_info.value.detail == "Invalid or missing API key"

    
        

