# Dependencies import
import pytest
from fastapi import HTTPException
from unittest.mock import patch

# File import
from src.Security.limiter import check_rate_limiter

# test api key unique ID (Passes)
def test_unique_keys_are_generated():
    with patch("src.Security.limiter.increment_counter") as mock_counter:
        mock_counter.return_value = 1
        check_rate_limiter("user_A")
        args_A, _ = mock_counter.call_args
        assert args_A[1] == "ratelimit:user_A"

        check_rate_limiter("user_B")
        args_B, _ = mock_counter.call_args
        assert args_B[1] == "ratelimit:user_B"

# test api key unique ID (Fails)
def test_same_keys_are_generated():
    with patch("src.Security.limiter.increment_counter") as mock_counter:
        mock_counter.return_value = 1

        check_rate_limiter("user_A")
        args_A, _ = mock_counter.call_args
    
        check_rate_limiter("user_A")
        args_B, _ = mock_counter.call_args

        assert args_A[1] == args_B[1]

# test rate limit (Passes)
def test_rate_limit_pass():
    with patch("src.Security.limiter.increment_counter") as mock_counter:
        mock_counter.return_value = 30

        result = check_rate_limiter("Test_User")

        assert result is True

# test rate limit (Fails)
def test_rate_limit_fail():
    with patch("src.Security.limiter.increment_counter") as mock_counter:
        mock_counter.return_value = 101

        with pytest.raises(HTTPException) as exec_info:
            check_rate_limiter("Test_User")

        assert exec_info.value.status_code == 429
        assert exec_info.value.detail == "Too Many Requests."


# test fail open (Redis error)
def test_redis_fail_open():
    with patch("src.Security.limiter.increment_counter") as mock_counter:
        mock_counter.return_value = 0

        result = check_rate_limiter("Test_User")

        assert result is True

