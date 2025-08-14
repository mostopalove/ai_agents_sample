from fastapi import APIRouter
from pydantic import BaseModel
from agents import Runner

from ai_agents.manager_agent import manager_agent

router = APIRouter(prefix="/ai", tags=["AI Translation Agents"])

class TranslateRequest(BaseModel):
    message: str

class TranslateResponse(BaseModel):
    response: str

@router.post("/translate", response_model=TranslateResponse)
async def translate_message(request: TranslateRequest):
    """
    Translate endpoint that receives a user message and translate it
    """
    user_message = request.message
    orchestrator_output = await Runner.run(manager_agent, user_message)

    return TranslateResponse(response=orchestrator_output.final_output)
