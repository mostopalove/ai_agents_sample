import random

from agents import Agent, function_tool


@function_tool
def get_farewell_message():
    farewells = [
        "Ara ara, sayonara!✌️",
        "Goodbye! See you later!👋",
        "Until we meet again, comrade!🫡",
        "Do svidaniya, Tovarisch!🤝"
    ]
    message = random.choice(farewells)
    print(f"I am going to use: {message}")
    return message


goodbye_agent_instructions = """
You are a friendly goodbye agent responsible for generating kind and context-appropriate farewell messages for users.
Use only the tools and resources available to you to create a farewell.
If no specific context is provided, use a default farewell such as "Thank you for chatting! Goodbye!"
If the input is unclear, generate a neutral, friendly farewell.
Do not perform tasks beyond generating a farewell message.
"""

goodbye_agent = Agent(
    name="GoodbyeAgent",
    instructions=goodbye_agent_instructions,
    tools=[get_farewell_message]
)
