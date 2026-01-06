from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings

# All variables assembled to one str
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Real connection to database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session since engine is not used in endpoints by standard practices
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class which all other created classes will inherit from
Base = declarative_base()
