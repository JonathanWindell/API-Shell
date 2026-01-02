import redis


def test_increment_counter_storage_success(mocker):
    """
    Ensure that increment is done correctly to prevent user from getting new token every call.
    """
    # Arrange
    mock_pipeline = mocker.Mock()

    mock_pipeline.execute.return_value = [1, -1]
    mock_client = mocker.Mock()

    mock_client.pipeline.return_value = mock_pipeline

    # Act
    from src.security.storage import increment_counter

    increment_counter(mock_client, "test_key")

    # Assert
    mock_client.expire.assert_called_with("test_key", 60)


def test_increment_counter_redis_error(mocker):
    """
    Ensure that increment is done correctly to prevent user from getting new token every call.
    """
    # Arrange
    mock_client = mocker.Mock()

    mock_client.pipeline.side_effect = redis.RedisError("Connection refused")

    # Act
    from src.security.storage import increment_counter

    result = increment_counter(mock_client, "user:123")

    # Assert
    assert result == 0
