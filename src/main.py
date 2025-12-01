from fastapi import FastAPI, Depends, Query
from src.Security.limiter import check_rate_limiter
from src.Classes.person_data import generate_german_person

app = FastAPI()

@app.get("/german-users")
def get_users(
    count: int = Query(1, ge=1, le=10, description="Max 10 persons"),
    limit_check: bool = Depends(check_rate_limiter) 
):
    return generate_german_person(count)
