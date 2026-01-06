from fastapi import Depends
from fastapi import APIRouter
from src.dependencies import get_db

# Create FastAPI router
router = APIRouter()


@router.get("/users")
def read_users(db_session=Depends(get_db)):
    """
    Endpoint for users. Open and closes connection when request is completed.

    args:
        get_db

    When creating functional API use db_session.query(...) to return queried data.
    """
    # return session with queried data
    return {"message": "Database connection works!"}
