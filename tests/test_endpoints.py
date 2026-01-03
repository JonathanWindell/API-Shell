def test_read_protected_route_success(client, valid_token):
    """
    Checks if /protected answers 200 of token is valid.
    """

    # Arrange
    auth_header = {"Authorization": f"Bearer {valid_token}"}

    # Act
    response = client.get("/protected", headers=auth_header)

    # Assert
    assert response.status_code == 200
    assert (
        response.json()["message"]
        == "You have successfully accessed a protected route!"
    )


def test_read_protected_route_no_token(client):
    """
    Validates that user without valid token is thrown out.
    """

    # Act
    response = client.get("/protected")

    # Assert
    assert response.status_code == 401


def test_router_auth_return(client):
    """
    Tests return from auth for correct formatting and data for router /token
    """

    # Arrange
    test_dict = {
        "username": "admin",
        "password": "secret",
    }

    # Act
    response = client.post("/token", data=test_dict)

    # Assert
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["token_type"]


def test_router_general_health_check_return(client):
    """
    Tests return health check for router /protected
    """

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json()["status"]


def test_login_failure(client):
    """
    Tests mocking of router /token
    """

    # Arrange
    test_dict = {
        "username": "admin",
        "password": "wrong_secret",
    }

    # Act
    response = client.post("/token", data=test_dict)

    # Assert
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"
