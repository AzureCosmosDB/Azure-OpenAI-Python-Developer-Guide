"""
API entrypoint for backend API.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from chat_session_state.cosmosdb_chat_session_state_provider import CosmosDBChatSessionStateProvider
from api_models.chat_session_request import ChatSessionResponse

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


# ========================
# Chat Session State / History Support is below:
# ========================

# Create an instance of the CosmosDBChatSessionStateProvider class
cosmos_provider = CosmosDBChatSessionStateProvider()

@app.get("/session/list", response_model=List[ChatSessionResponse])
def list_sessions():
    """
    Endpoint to list all chat sessions.
    """
    try:
        return cosmos_provider.list_sessions()
    except RuntimeError as e:
        # Return an internal server error if a runtime error occurs
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/session/load/{session_id}")
def load_session(session_id: str):
    """
    Endpoint to load a chat session by session_id.
    """
    try:
        return cosmos_provider.load_session(session_id)
    except ValueError as e:
        # Return a 404 error if the session is not found
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        # Return an internal server error if a runtime error occurs
        raise HTTPException(status_code=500, detail=str(e))
