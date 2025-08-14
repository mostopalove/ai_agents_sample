from agents import Runner
from fastapi import APIRouter
from pydantic import BaseModel

from greeting_agent.main_agent import main_agent

router = APIRouter(prefix="/greeting", tags=["AI Greeting Agents"])


class GreetingRequest(BaseModel):
    message: str


@router.post("/say-hi")
async def say_greeting(request: GreetingRequest):
    user_message = request.message
    orchestrator_output = await Runner.run(main_agent, user_message)
    return orchestrator_output.final_output
