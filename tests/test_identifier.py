import pytest
from fastapi import HTTPException
from src.security.identifier import get_and_validate_key
from src.security import settings 

# test valid key
@pytest.mark.asyncio
async def test_valid_api_key():
    settings.VALID_API_KEY = {"Test_Api_Key"}
    result = await get_and_validate_key("Test_Api_Key")

    assert result == "Test_Api_Key"

# test invalid key
@pytest.mark.asyncio
async def test_invalid_api_key():
    settings.VALID_API_KEY = {"Test_Api_Key"}

    with pytest.raises(HTTPException) as exec_info:
        await get_and_validate_key("Wrong_Api_Key")

    assert exec_info.value.status_code == 401
    assert exec_info.value.detail == "Invalid or missing API key"

    
        

