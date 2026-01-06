from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter
from typing import Annotated

from src.config import settings
from src.auth.user_manager import UserManager

# Create FastAPI router
router = APIRouter()


# Dependency Injection
def get_user_manager():
    return UserManager()  # pragma: no cover


# Create route
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
):
    """
    Login endpoint. authenticates user and returns a JWT token.
    """
    # Mock userbase
    fake_db_user = settings.db_user
    fake_db_hash_password = settings.db_hash_password

    fake_db_hash = user_manager.get_password_hash(fake_db_hash_password)

    if form_data.username != fake_db_user or not user_manager.verify_password(
        form_data.password, fake_db_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = user_manager.create_access_token(data={"sub": form_data.username})

    return {"access_token": access_token, "token_type": "bearer"}
