from agents import Agent, WebSearchTool, Runner

from ai_clients.open_ai.sub_agents.query_optimization_agent import QueryOptimizationClient
from common.classes import AIClient
from prompts.master_agent_prompt import master_agent_prompt


class OpenAIClient(AIClient):
    def __init__(self):
        self.client = None
        self.optimization_agent = QueryOptimizationClient()

    async def setup(self):
        await self.optimization_agent.setup()
        self.client = Agent(
            name="master_agent",
            instructions=master_agent_prompt,
            tools=[
                WebSearchTool(),
                self.optimization_agent.client.as_tool(
                    tool_name="bigquery_query_optimizer_ai_agent",
                    tool_description="This AI agent optimizes Google BigQuery SQL queries for performance and cost. It analyzes queries, identifies inefficiencies, and provides rewritten versions with clear explanations.",
                )
            ]
        )

    async def destroy(self):
        await self.optimization_agent.destroy()

    async def chat(self, user_request: str):
        if self.client is None:
            raise Exception("Client is not initialized, run setup method first")

        result = await Runner.run(self.client, user_request)
        return result.final_output
