# Dependencies import
from faker import Faker
from fastapi import FastAPI, Query

@app.get("/person")
def generate_german_person(
    count: int = Query(1, ge=1, le=10, description="Number of persons to generate (max 10)")
):
    fake = Faker("de_DE")
    persons = []
    for _ in range(count):
        persons.append({
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "tax_id": fake.ssn(),  # In Germany: Steueridentifikationsnummer
            "nationality": "Deutsch"
        })
    return {"data": persons}