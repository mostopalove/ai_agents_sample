from abc import ABC, abstractmethod
from typing import Type


class AIClient(ABC):
    @abstractmethod
    async def chat(self, user_request: str):
        """The general method to call main AI assistant"""
        pass

    @abstractmethod
    def setup(self):
        """Initialization agent with sub-agents and internal tools like MCP servers"""
        pass


class AIAssistant:
    def __init__(self, client: Type[AIClient]):
        self.client = client()
        self.client.setup()

    async def chat(self, user_request: str):
        return await self.client.chat(user_request)