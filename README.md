# API Shell

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-Cache-red?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-yellow?logo=pytest&logoColor=white)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![ReadMe](https://img.shields.io/badge/ReadMe-018EF5?logo=readme&logoColor=fff)
![License](https://img.shields.io/badge/License-MIT-green)

# Highlights

This project was created as an easier way to create API:s. The base of the API often consists of the same modules which led me to create this project!

- **Rate Limiting:** Protects endpoints using Redis to prevent abuse (Sliding Window algorithm).
- **Secure Auth:** Full JWT implementation with Bcrypt password hashing.
- **TDD Architecture:** Built from the ground up using Test Driven Development with Pytest.

# Overview

I created this project because I noticed I was rewriting the same "boilerplate" code for every new API I started. As a System Science student, I wanted a robust, secure, and tested shell that allows me (and others) to focus on business logic instead of setup.

This shell provides the essential building blocks—Security, Auth, and Storage—pre-wired and ready to go.

# Author

I'm Jonathan and I develop projects in my sparetime that help myself and others being better and more efficient developers!
- [Linkedin](https://www.linkedin.com/in/jonathan-windell-418a55232/)
- [Portfolio](https://portfolio.jonathans-labb.org/)

# Project Structure

```text
├── .github/
│   └── workflows/      # CI/CD Pipelines (GitHub Actions)
├── src/
│   ├── auth/           # Authentication logic & User Manager
│   ├── core/           # Core infrastructure (Config, Database, Exceptions)
│   ├── models/         # Pydantic Schemas & Data Models
│   ├── routers/        # API Routes/Endpoints
│   ├── security/       # Security logic (Rate limiting, Identifier)
│   └── dependencies.py # Dependency Injection helpers
├── tests/              # Test suite (Pytest)
├── .env                # Environment variables (Configuration)
├── docker-compose.yml  # Docker services setup
├── Dockerfile          # Container definition
├── main.py             # Application entry point
└── requirements.txt    # Python dependencies
```

# Usage Instructions

Since this is an API Shell, it comes with a fully functional Authentication flow and Rate Limiting enabled by default.

### 1. Accessing the API Documentation
Once the server is running, navigate to:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


### 2. How to add a new Protected Route
This shell comes with a built-in `user_manager` and dependency injection system. Here is how you create a new secure endpoint:

```python
from fastapi import APIRouter, Depends
from src.auth.user_manager import UserManager
from src.dependencies import get_user_manager

router = APIRouter()

@router.get("/my-secure-endpoint")
def secure_data(
    user_manager: UserManager = Depends(get_user_manager)
):
    return {"message": "You are authenticated!", "user": "secure_user"}
```

### 3. Useful Documentation & Resources
### SQLAlchemy
This API Shell leverages **SQLAlchemy** for robust database interactions and ORM (Object-Relational Mapping). It allows you to work with database records seamlessly using Python objects. If you are new to SQLAlchemy or want to deepen your understanding of the implementation, I highly recommend these resources:

- [Official SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [ArjanCodes - SQLAlchemy Guide](https://www.youtube.com/watch?v=aAy-B6KPld8)

### Pydantic
**Pydantic** is used throughout the project to enforce strict data validation and schema definitions for all API endpoints. This ensures that incoming and outgoing data is always consistent and type-safe. To learn more about its powerful features, check out:

- [Official Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Pixegami - Pydantic Tutorial](https://www.youtube.com/watch?v=XIdQ6gO3Anc)

# Installation Instructions

### Prerequisites
- Docker Desktop (Recommended)
- Python 3.12 and local Redis instance (Local Development)

**Tips:** Always easier creating a virtual environment to contain downloaded dependencies needed for this project if you will develop locally. [W3School Venv](https://www.w3schools.com/python/python_virtualenv.asp)

### Docker Compose (Fastest)
```bash
# 1. Clone the repository
git clone https://github.com/JonathanWindell/API-Shell.git

# 2. Start the services
docker-compose up --build
```

### Local Development
``` Bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload
```
### Configuration
Create a `.env` file in the root directory. You can copy the structure below:

```ini
# Security
SECRET_KEY=your_super_secret_key_change_this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=postgres
DATABASE_NAME=postgres
DATABASE_USERNAME=postgres

# Rate Limiting (Redis)
RATE_LIMIT_LIMIT=5
RATE_LIMIT_WINDOW=60

```

# Contributions

Contributions are welcome! Since this project follows **TDD (Test Driven Development)**, please ensure you include tests for any new features.

1. **Fork** the project.
2. Create your Feature Branch (`git checkout -b feature/UserFeature`).
3. Commit your changes (`git commit -m 'Add some Feature'`).
4. **Run Tests** (`pytest`). Ensure everything is green! 
5. Push to the Branch (`git push origin feature/UserFeature`).
6. Open a **Pull Request**.

# License

Distributed under the MIT License. See `LICENSE` file for more information.


