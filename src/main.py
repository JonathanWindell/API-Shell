from fastapi import FastAPI, Query
from faker import Faker

app = FastAPI(
    title="German Personal Data Generator",
    description="Generate realistic German fake personal data for testing (GDPR-safe).",
    version="0.1.0"
)

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