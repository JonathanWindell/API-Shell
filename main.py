from fastapi import FastAPI

from src.routers.general_router import router as general_router
from src.routers.auth_router import router as auth_router
from src.routers.database_router import router as database_router


# Create FastAPI app
app = FastAPI(title="API Shell")

# Include routers
app.include_router(auth_router)
app.include_router(general_router)
app.include_router(database_router)
