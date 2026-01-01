import redis
import logging
import os

from redis import Redis


def establish_redis_connection() -> Redis:
    """
    Establish a connection to Redis.

    Returns:
        redis.Redis: The Redis client.
    """
    redis_host = os.getenv("REDIS_HOST", "localhost")

    return redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)


def increment_counter(client: Redis, key: str, window_seconds: int = 60) -> int:
    """
    Increment the counter for the given key within the specified window.

    Args:
        client (redis.Redis): The Redis client.
        key (str): The key to increment.
        window_seconds (int, optional): The window size in seconds. Defaults to 60.

    Returns:
        int: The current count for the key.

    Raises:
        redis.RedisError: If there is a Redis error.
    """
    try:
        pipeline = client.pipeline()

        pipeline.incr(key)
        pipeline.ttl(key)

        result = pipeline.execute()
        current_count = result[0]
        current_ttl = result[1]

        if current_ttl == -1:
            client.expire(key, window_seconds)

        return current_count
    except redis.RedisError as e:
        logging.error(f"Redis error {e}")
        return 0


redis_client = establish_redis_connection()

if __name__ == "__main__":
    print(increment_counter(redis_client, "ratelimit:test_user"))
