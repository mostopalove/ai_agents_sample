from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from prompts.bigquery_optimization_agent_prompt import bigquery_optimization_agent_prompt

optimization_agent = LlmAgent(
    name="optimization_agent",
    instruction=bigquery_optimization_agent_prompt,
    description="This AI agent optimizes Google BigQuery SQL queries for performance and cost. It analyzes queries, identifies inefficiencies, and provides rewritten versions with clear explanations.",
    tools=[google_search],
)
