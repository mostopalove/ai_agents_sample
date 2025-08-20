from agents import Agent, WebSearchTool

from prompts.bigquery_optimization_agent_prompt import bigquery_optimization_agent_prompt

optimization_agent = Agent(
    name="optimization_agent",
    instructions=bigquery_optimization_agent_prompt,
    tools=[WebSearchTool()],
)
