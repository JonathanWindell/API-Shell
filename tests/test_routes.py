from src.routers import auth, general


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

    # Arrange
    auth_header = {"Authorization"}

    # Act
    response = client.get("/protected")

    # Assert
    assert response.status_code == 401
