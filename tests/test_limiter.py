# Dependencies import
import pytest
from fastapi import HTTPException
from unittest.mock import patch

# File import
from src.Security.limiter import check_rate_limiter, increment_counter

# test api key unique ID (Passes)
def test_unique_keys_are_generated():
    mock_counter = increment_counter

    result = mock_counter(1)
    check_rate_limiter("user_A")

    assert mock_counter == "ratelimit:user_A"

    check_rate_limiter("user_B")

    assert mock_counter == "ratelimit:user_B"

    return result

# test api key unique ID (Fails)
"""
create valid_api_key with ID 1
create valid_api_key with ID 1

raise error given that duplicate exist

assert result detail ID is the same
"""

# test rate limit (Passes)
"""
create number_of_calls = 30

assert number_of_calls is within accepted limits

assert result = number_of_calls is ok
"""

# test rate limit (Fails)
"""
create number_of_calls = 130

assert number_of_calls is outside accepted limits

raise error given that number_of_calls is outside range

assert http 429
assert detail = "Too Many Requests
"""

# test fail open (Redis error)