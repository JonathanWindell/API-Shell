# Dependencies import
import os
from dotenv import load_dotenv

load_dotenv()

# Get keys from .env file and set as enviroment variables
_keys_string = os.getenv("API_KEYS", "test_key_1")

# Split VALID_API_KEY to only get key
VALID_API_KEY = set(_keys_string.split(","))

# Sets rates. Will be expanded upon for different users.  
RATE_LIMIT_LIMIT = 100
RATE_LIMIT_WINDOW = 60


