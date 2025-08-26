from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router as main_router
from assistant_agent_module.routes import router as ai_agent_router
from agents import enable_verbose_stdout_logging

load_dotenv()

enable_verbose_stdout_logging()

app = FastAPI(
    title="FastAPI Project with sample of AI Agents",
    description="A FastAPI project with small examples of using AI agents",
    version="1.0.0"
)

app.include_router(main_router)
app.include_router(ai_agent_router)
