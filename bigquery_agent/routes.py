from agents import Runner
from fastapi import APIRouter
from pydantic import BaseModel

from bigquery_agent.bigquery_agent import bigquery_agent

router = APIRouter(prefix="/bigquery", tags=["BigQuery"])


class QueryHandlerRequest(BaseModel):
    message: str


@router.post("/query")
async def query_handler(request: QueryHandlerRequest):
    user_request = request.message
    orchestrator_output = await Runner.run(bigquery_agent, user_request)
    return orchestrator_output.final_output
