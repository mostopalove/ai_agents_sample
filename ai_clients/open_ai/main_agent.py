from agents import Agent, WebSearchTool, Runner

from ai_clients.open_ai.sub_agents.optimization_agent import optimization_agent
from common.classes import AIClient
from prompts.main_agent_prompt import main_agent_prompt


class OpenAIClient(AIClient):
    def __init__(self):
        self.client = None

    def setup(self):
        self.client = Agent(
            name="bigquery_agent",
            instructions=main_agent_prompt,
            tools=[
                optimization_agent.as_tool(
                    tool_name="bigquery_query_optimizer_ai_agent",
                    tool_description="This AI agent optimizes Google BigQuery SQL queries for performance and cost. It analyzes queries, identifies inefficiencies, and provides rewritten versions with clear explanations.",
                ),
                WebSearchTool()
            ]
        )

    async def chat(self, user_request: str):
        if self.client is None:
            raise Exception("Client is not initialized, run setup method first")

        result = await Runner.run(self.client, user_request)
        return result.final_output
