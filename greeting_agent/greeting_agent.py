import random

from agents import Agent, function_tool


@function_tool
def get_greeting_message():
    greetings = [
        "Konnichiwa senpai!✌️",
        "Hello there!👋",
        "Salute, comrade!🫡",
        "Privet Tovarisch!🤝"
    ]
    message = random.choice(greetings)
    print(f"I am going to use: {message}")
    return message

greeting_agent_instructions = """
You are a friendly greeting agent responsible for generating kind and context-appropriate greeting messages for users.
Use only the tools and resources available to you to create a greeting.
If no specific context is provided, use a default greeting such as "Hello! It's nice to see you!"
If the input is unclear, generate a neutral, friendly greeting.
Do not perform tasks beyond generating a greeting message.
"""

greeting_agent = Agent(
    name="GreetingAgent",
    instructions=greeting_agent_instructions,
    tools=[get_greeting_message]
)
