# Dependencies import
import redis
import logging
import os

# Instantiate a Redis client, connecting to redis host on port 6379. 
def establish_redis_connection():
    redis_host = os.getenv("REDIS_HOST", "localhost")

    return redis.Redis(
        host=redis_host,
        port=6379,
        db=0,
        decode_responses=True
    )

# Creates a counter that keeps track of client usage. 
def increment_counter(client, key, window_seconds=60):
    try:
        pipeline = client.pipeline()

        pipeline.incr(key)
        pipeline.expire(key, window_seconds) # Fix this. Sliding window effect. 

        result = pipeline.execute()
        current_count = result[0]

        return current_count
    except redis.RedisError as e:
        logging.error(f"Redis error {e}")
        return 0
    
redis_client = establish_redis_connection()

if __name__ == "__main__":
    print(increment_counter(redis_client, "ratelimit:test_user"))
