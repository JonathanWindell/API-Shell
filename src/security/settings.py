import os
from dotenv import load_dotenv

load_dotenv()

"""
Application Configuration
"""

# Get keys from .env file and set as enviroment variables
_keys_string = os.getenv("API_KEYS", "test_key_1")

# Split VALID_API_KEY to only get key
VALID_API_KEYS = {key.strip() for key in _keys_string.split(",")}

# Rate limiting constants
RATE_LIMIT_LIMIT = 3
RATE_LIMIT_WINDOW = 60


