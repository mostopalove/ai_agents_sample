from agents import Agent
from .translator_agents import russian_agent, ukrainian_agent


manager_agent = Agent(
    name="ManagerAgent",
    instructions="You are a manager agent that can coordinate the translation agents. Your aim is translate the message to the Russian and Ukrainian languages.",
    tools=[
        russian_agent.as_tool(
            tool_name="translate_to_russian",
            tool_description="Translate the message to the Russian language",
        ),
        ukrainian_agent.as_tool(
            tool_name="translate_to_ukrainian",
            tool_description="Translate the message to the Ukrainian language",
        ),
    ]
)