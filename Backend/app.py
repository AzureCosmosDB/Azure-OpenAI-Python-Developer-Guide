"""
API entrypoint for backend API.
"""
from fastapi import FastAPI, HTTPException
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


# ========================
# Chat Session State / History Support is below:
# ========================
import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient
from pydantic import BaseModel
from typing import List

load_dotenv()

# Your existing Cosmos DB client and container setup
CONNECTION_STRING = os.environ.get("COSMOS_DB_CONNECTION_STRING")
client = CosmosClient.from_connection_string(CONNECTION_STRING)
db = client.get_database_client("cosmic_works")
chat_session_container = db.get_container_client("chat_session")

# Define the model for a Chat Session response
class ChatSessionResponse(BaseModel):
    session_id: str
    title: str

@app.get("/session/list") #, response_model=List[ChatSessionResponse])
def list_sessions():
    """
    Endpoint to list all chat sessions.
    """
    try:
        # Query to get all sessions in the chat_session_container
        query = "SELECT c.id, c.title FROM c"
        sessions = list(chat_session_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        
        # Convert the sessions into a list of ChatSessionResponse objects
        session_responses = [ChatSessionResponse(session_id=session['id'], title=session['title']) for session in sessions]
        return session_responses
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve sessions: {str(e)}")

# GET /session/load/{session_id}
@app.get("/session/load/{session_id}")
def load_session(session_id: str):
    """
    Endpoint to load a chat session by session_id.
    """
    try:
        # Query to get the chat session with the provided session_id
        query = f"SELECT * FROM c WHERE c.id = '{session_id}'"
        session = list(chat_session_container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        
        # If the session exists, return it
        if session:
            return session[0]
        else:
            raise HTTPException(status_code=404, detail="Session not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve session: {str(e)}")
    
    