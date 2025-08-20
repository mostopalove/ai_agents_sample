from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types # For creating message Content/Parts

from ai_clients.google.sub_agents.optimization_agent import optimization_agent
from common.classes import AIClient
from prompts.main_agent_prompt import main_agent_prompt


class GoogleAIClient(AIClient):
    def __init__(self):
        self.client = None
        self.session_service = None
        # Define constants for identifying the interaction context
        self.APP_NAME = "ai_assistant_app"
        self.USER_ID = "user_1"
        self.SESSION_ID = "session_001"  # Using a fixed ID for simplicity

    def setup(self):
        # --- Session Management ---
        # Key Concept: SessionService stores conversation history & state.
        self.session_service = InMemorySessionService()
        self.client = LlmAgent(
            model="gemini-2.0-flash",
            name="bigquery_agent",
            instruction=main_agent_prompt,
            sub_agents=[optimization_agent],
            tools=[google_search]
        )

    async def chat(self, user_request: str):
        if self.client is None:
            raise Exception("Client is not initialized, run setup method first")

        # Create the specific session where the conversation will happen
        session = await self.session_service.create_session(
            app_name=self.APP_NAME,
            user_id=self.USER_ID,
            session_id=self.SESSION_ID
        )

        # --- Runner ---
        # Key Concept: Runner orchestrates the agent execution loop.
        runner = Runner(
            agent=self.client,  # The agent we want to run
            app_name=self.APP_NAME,  # Associates runs with our app
            session_service=self.session_service  # Uses our session manager
        )

        # Prepare the user's message in ADK format
        content = types.Content(role='user', parts=[types.Part(text=user_request)])

        final_response_text = ""

        # Key Concept: run_async executes the agent logic and yields Events.
        # We iterate through events to find the final answer.
        async for event in runner.run_async(user_id=self.USER_ID, session_id=self.SESSION_ID, new_message=content):
            # You can uncomment the line below to see *all* events during execution
            # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

            # Key Concept: is_final_response() marks the concluding message for the turn.
            if event.is_final_response():
                if event.content and event.content.parts:
                    # Assuming text response in the first part
                    final_response_text = event.content.parts[0].text
                elif event.actions and event.actions.escalate:  # Handle potential errors/escalations
                    final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
                # Add more checks here if needed (e.g., specific error codes)
                break  # Stop processing events once the final response is found

        return final_response_text

