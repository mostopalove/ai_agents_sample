from fastapi import APIRouter
from pydantic import BaseModel

from ai_clients.open_ai.master_agent import OpenAIClient
from common.classes import AIAssistant

router = APIRouter(prefix="/agent", tags=["AI Agent"])


class AssistRequest(BaseModel):
    message: str


@router.post("/assist")
async def query_handler(request: AssistRequest):
    user_request = request.message
    ai_assistant = AIAssistant(client=OpenAIClient)
    response = await ai_assistant.chat(user_request)
    return response
