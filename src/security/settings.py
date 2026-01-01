import os
from dotenv import load_dotenv

load_dotenv()

"""
Application Configuration
"""

# Get keys from .env file. Default to "test_key_1" if not found.
# NOTE: In .env, this should be named API_KEYS (plural)
_keys_string = os.getenv("API_KEYS", "test_key_1")

# Split VALID_API_KEY to only get actual key
VALID_API_KEYS = {key.strip() for key in _keys_string.split(",")}

# Rate limiting constants
RATE_LIMIT_LIMIT = int(os.getenv("RATE_LIMIT_LIMIT", 3))
RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", 60))
