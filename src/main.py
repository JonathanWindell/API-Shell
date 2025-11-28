from fastapi import FastAPI, Query
from src.Classes.person_data import generate_german_person

app = FastAPI(
    title="German Personal Data Generator",
    description="Generate realistic German fake personal data for testing (GDPR-safe).",
    version="0.1.0"
)

