
from logging import getLogger
from fastapi import HTTPException, status, Depends

# File import
from src.Security.identifier import get_and_validate_key
from src.Security.storage import increment_counter, redis_client
from src.Security.settings import RATE_LIMIT_LIMIT, RATE_LIMIT_WINDOW

logger = getLogger(__name__)

def check_rate_limiter(api_key: str = Depends(get_and_validate_key)):
    # Create unique API key ID to not create 
    unique_api_key_id = f"ratelimit:{api_key}"

    # Calls on increment counter and gives information and increments
    number_of_calls = increment_counter(redis_client, unique_api_key_id, RATE_LIMIT_WINDOW)
    
    # Checks if number of calls is 0. If that is the case there might be errors on service end
    if number_of_calls == 0:
        logger.warning("Unfortunately there seems to be a problem.")
        return True
    
    # Check number of calls for rate limit. If true raise HTTP_429_TOO_MANY_REQUESTS
    if number_of_calls > RATE_LIMIT_LIMIT:
        raise HTTPException(
            status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too Many Requests."
        )
    # If everything passes return true and allow user request.  
    return True

