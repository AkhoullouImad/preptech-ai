from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class InterviewRequest(BaseModel):
    cv: str
    job_description: str
    type: str  # "hr" or "technical"

@router.post("/start")
def start_interview(request: InterviewRequest):
    return {
        "question": f"Starting {request.type} interview. Tell me about yourself."
    }