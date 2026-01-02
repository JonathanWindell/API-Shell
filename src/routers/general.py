from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from typing import Annotated

from src.auth.user_manager import UserManager
from src.security.limiter import check_rate_limiter

# Create FastAPI router
router = APIRouter()


# Dependency Injection
def get_user_manager():
    return UserManager()


# Create OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Create routes
@router.get("/protected")
async def read_protected_route(
    _token: Annotated[str, Depends(oauth2_scheme)],
    _allowed: bool = Depends(check_rate_limiter),
):
    """
    A protected route. Requires a valid JWT token and is Rate Limited.
    """
    return {
        "username": "admin",
        "message": "You have successfully accessed a protected route!",
    }


@router.get("/")
def health_check():
    return {"status": "System is running", "docs": "Go to /docs to test the API"}
