from fastapi import FastAPI
from app.api import interview

app = FastAPI()

app.include_router(interview.router, prefix="/interview")

@app.get("/")
def root():
    return {"message": "PrepTechAI is running"}