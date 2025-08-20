from fastapi import APIRouter
from pydantic import BaseModel

from ai_clients.open_ai.main_agent import OpenAIClient
from common.classes import AIAssistant

router = APIRouter(prefix="/bigquery", tags=["BigQuery"])


class QueryHandlerRequest(BaseModel):
    message: str


@router.post("/query")
async def query_handler(request: QueryHandlerRequest):
    user_request = request.message
    ai_assistant = AIAssistant(client=OpenAIClient)
    response = await ai_assistant.chat(user_request)
    return response
