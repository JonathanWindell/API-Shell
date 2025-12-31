from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from src.auth.user_manager import UserManager
from src.security.limiter import check_rate_limiter
from src.models.schemas import Token, UserResponse  

# 1. Initialize
app = FastAPI(
    title="API Shell",
    description="A secure boilerplate with JWT Auth and Redis Rate Limiting.",
    version="1.0.0"
)

# 2. Swagger UI setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 3. Dependency Injection
def get_user_manager():
    return UserManager()

# 4. Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_manager: Annotated[UserManager, Depends(get_user_manager)]
):
    """
    Login endpoint. authenticates user and returns a JWT token.
    """
    # Mockad användardatabas för detta shell
    fake_db_user = "admin"
    fake_db_hash = user_manager.get_password_hash("secret") 

    if form_data.username != fake_db_user or not user_manager.verify_password(form_data.password, fake_db_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = user_manager.create_access_token(
        data={"sub": form_data.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/protected", response_model=UserResponse)
async def read_protected_route(
    token: Annotated[str, Depends(oauth2_scheme)], 
    allowed: bool = Depends(check_rate_limiter)
):
    """
    A protected route. Requires a valid JWT token and is Rate Limited.
    """
    return {
        "username": "admin", 
        "message": "You have successfully accessed a protected route!"
    }

@app.get("/")
def health_check():
    return {"status": "System is running", "docs": "Go to /docs to test the API"}