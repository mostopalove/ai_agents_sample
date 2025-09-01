from agents import Agent, WebSearchTool, Runner
from agents.mcp import MCPServerStreamableHttp

from common.classes import AIClient
from prompts.bigquery.query_optimization_agent_prompt import query_optimization_agent_prompt

query_optimization_agent = Agent(
    name='query_optimization_agent',
    instructions=query_optimization_agent_prompt,
    tools=[
        WebSearchTool(),
    ]
)


class QueryOptimizationClient(AIClient):
    def __init__(self):
        self.client = None
        self.bq_mcp_server = MCPServerStreamableHttp(
            name="mcp_bigquery_server",
            params={
                "url": "http://127.0.0.1:5000/mcp",
            }
        )

    async def setup(self):
        try:
            await self.bq_mcp_server.connect()
        except Exception as e:
            raise Exception(f"Failed to connect to MCP BigQuery server: {e}")

        self.client = Agent(
            name='query_optimization_agent',
            model="gpt-5",
            instructions=query_optimization_agent_prompt,
            tools=[
                WebSearchTool(),
            ],
            mcp_servers=[self.bq_mcp_server]
        )

    async def destroy(self):
        await self.bq_mcp_server.cleanup()

    async def chat(self, user_request: str):
        if self.client is None:
            raise Exception("Client is not initialized, run setup method first")

        result = await Runner.run(self.client, user_request)
        return result.final_output
