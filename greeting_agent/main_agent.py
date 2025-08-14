from agents import Agent

from greeting_agent.goodbye_agent import goodbye_agent
from greeting_agent.greeting_agent import greeting_agent

main_agent_instruction = """
You are a kind and friendly main agent responsible for coordinating greetings or goodbyes for users by delegating to specialized greeting or goodbye agents.
Based on user input, determine whether a greeting or goodbye is appropriate.
Select the corresponding agent (greeting agent for hellos, goodbye agent for farewells) and ensure they deliver a context-appropriate message.
If no specialized agent is available, provide a default kind greeting (e.g., 'Hello! How can I assist you today?') or goodbye (e.g., 'Thank you for chatting! Goodbye!').
"""

main_agent = Agent(
    name="MainAgent",
    instructions=main_agent_instruction,
    tools=[
        greeting_agent.as_tool(
            tool_name="greeting_agent",
            tool_description="Agent that provides greeting message to user",
        ),
        goodbye_agent.as_tool(
            tool_name="goodbye_agent",
            tool_description="Agent that provides goodbye message to user",
        )
    ]
)
