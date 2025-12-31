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


# Usage Instructions

Since this is an API Shell, it comes with a fully functional Authentication flow and Rate Limiting enabled by default.

# Installation Instructions

### Prerequisites
- Docker Desktop (Recommended)
- Python 3.12 and local Redis instance (Local Development)

**Tips:** Always easier creating a virtual enviroment to contain downloaded dependencies needed for this project if you will develop locally. [W3School Venv](https://www.w3schools.com/python/python_virtualenv.asp)

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


