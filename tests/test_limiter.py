import pytest
from fastapi import HTTPException
from unittest.mock import patch

from src.security.limiter import check_rate_limiter

def test_redis_key_generation_logic():
    """
    Verifies that the rate limiter generates unique Redis keys 
    formatted correctly for different users.
    """
    with patch("src.security.limiter.increment_counter") as mock_counter:
        # Arrange
        mock_counter.return_value = 1  

        # Act
        check_rate_limiter("user_A")
        check_rate_limiter("user_B")

        # Assert
        calls = mock_counter.call_args_list
        
        assert len(calls) == 2
        
        # calls[0] is the first call (user_A)
        # .args[1] is the second argument (key)
        assert calls[0].args[1] == "ratelimit:user_A"
        
        # calls[1] is the second call (user_B)
        assert calls[1].args[1] == "ratelimit:user_B"

def test_rate_limit_pass():
    """
    Verifies that the request is allowed (Returns True) 
    when the call count is within the limit.
    """
    with patch("src.security.limiter.increment_counter") as mock_counter:
        # Arrange
        mock_counter.return_value = 3

        # Act
        result = check_rate_limiter("Test_User")

        # Assert
        assert result is True

def test_rate_limit_exceeded():
    """
    Verifies that an HTTPException (429) is raised 
    when the call count exceeds the limit.
    """
    with patch("src.security.limiter.increment_counter") as mock_counter:
        # Arrange
        mock_counter.return_value = 101

        # Act
        with pytest.raises(HTTPException) as exec_info:
            check_rate_limiter("Test_User")

        # Assert
        assert exec_info.value.status_code == 429
        assert exec_info.value.detail == "Too Many Requests."

def test_redis_fail_open():
    """
    Verifies the 'Fail Open' strategy: 
    If Redis returns 0 (connection error), the user should still be allowed through.
    """
    with patch("src.security.limiter.increment_counter") as mock_counter:
        # Arrange
        mock_counter.return_value = 0

        # Act
        result = check_rate_limiter("Test_User")

        # Assert
        assert result is True

