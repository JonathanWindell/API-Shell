import redis
import logging
import os

# Instantiate a Redis client, connecting to localhost on port 6379
def establish_redis_connection():
    redis_host = os.getenv('REDIS_HOST', 'localhost')

    return redis.Redis(
        host=redis_host,
        port=6379,
        db=0,
        decode_responses=True
    )

def increment_counter(client, key, window_seconds=60):
    try:
        pipeline = client.pipeline()

        pipeline.incr(key)
        pipeline.expire(key, window_seconds)

        result = pipeline.execute()
        current_count = result[0]

        return current_count
    except redis.RedisError as e:
        logging.error(f"Redis error {e}")
        return 0

redis_client = establish_redis_connection()
user_key = "my_key"
increment_counter(redis_client, user_key)
