from logging import getLogger
from fastapi import HTTPException, status, Depends

from src.security.identifier import get_and_validate_key
from src.security.storage import increment_counter, redis_client
from src.security.settings import RATE_LIMIT_LIMIT, RATE_LIMIT_WINDOW

logger = getLogger(__name__)

def check_rate_limiter(api_key: str = Depends(get_and_validate_key)) -> bool:
    """
    Checks the rate limit of the API key. 

    If the Redis counter fails (returns 0), the system defaults to 'Fail Open' 
    (allowing the request) to prevent blocking users during infrastructure issues.

    Args:
        api_key (str): The API key extracted from the 'x-api-key' header.
        
    Returns:
        bool: True if the rate limit is not exceeded, False otherwise.

    Raises:
        Warning: If number_of_calls is 0.
        HTTPException: If the rate limit is exceeded.
    """
    unique_api_key_id = f"ratelimit:{api_key}"

    number_of_calls = increment_counter(redis_client, unique_api_key_id, RATE_LIMIT_WINDOW)
    
    if number_of_calls == 0:
        logger.warning("Unfortunately there seems to be a problem.")
        return True
    
    if number_of_calls > RATE_LIMIT_LIMIT:
        raise HTTPException(
            status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too Many Requests."
        )
  
    return True

