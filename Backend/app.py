"""
API entrypoint for backend API.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uuid

from api_models.ai_request import AIRequest
from cosmic_works.cosmic_works_ai_agent import CosmicWorksAIAgent

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Agent pool keyed by session_id to retain memories/history in-memory.
# Note: the context is lost every time the service is restarted.
agent_pool = {}

@app.get("/")
def root():
    """
    Health probe endpoint.
    """
    return {"status": "ready"}

@app.post("/ai")
def run_cosmic_works_ai_agent(request: AIRequest):
    """
    Run the Cosmic Works AI agent.
    """
    prompt = request.prompt
    session_id = request.session_id

    # If no session_id is provided or default is provided, generate a new one.
    if (session_id is None or session_id == "1234"):
        session_id = str(uuid.uuid4())

    # If the session_id is not in the agent pool, create a new agent.
    if session_id not in agent_pool:
        agent_pool[session_id] = CosmicWorksAIAgent(session_id)

    # Run the agent with the provided prompt.
    return { "message": agent_pool[session_id].run(prompt), "session_id": session_id }
