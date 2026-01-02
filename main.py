from fastapi import FastAPI

from src.routers.general import router as general_router
from src.routers.auth import router as auth_router

# Create FastAPI app
app = FastAPI(title="API Shell")

# Include routers
app.include_router(auth_router)
app.include_router(general_router)
