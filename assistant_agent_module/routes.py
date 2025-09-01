from fastapi import APIRouter, Body

from ai_clients.open_ai.master_agent import OpenAIClient
# from ai_clients.open_ai.sub_agents.query_optimization_agent import QueryOptimizationClient
from common.classes import AIAssistant

router = APIRouter(prefix="/agent", tags=["AI Agent"])


@router.post("/assist")
async def query_handler(user_request: str = Body(..., media_type="text/plain")):
    ai_assistant = AIAssistant(client=OpenAIClient)
    await ai_assistant.initialize()
    response = await ai_assistant.chat(user_request)
    await ai_assistant.cleanup()
    return response
