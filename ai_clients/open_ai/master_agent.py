from agents import Agent, WebSearchTool, Runner

from common.classes import AIClient
from prompts.master_agent_prompt import master_agent_prompt


class OpenAIClient(AIClient):
    def __init__(self):
        self.client = None

    def setup(self):
        self.client = Agent(
            name="master_agent",
            instructions=master_agent_prompt,
            tools=[
                WebSearchTool()
            ]
        )

    async def chat(self, user_request: str):
        if self.client is None:
            raise Exception("Client is not initialized, run setup method first")

        result = await Runner.run(self.client, user_request)
        return result.final_output
