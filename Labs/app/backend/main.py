"""
API entrypoint for backend API.
"""
import uvicorn
from fastapi import FastAPI
from api_models.ai_request import AIRequest
from cosmic_works.cosmic_works_ai_agent import CosmicWorksAIAgent

app = FastAPI()
# Agent pool keyed by session_id to retain memories/history in-memory.
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
    if request.session_id not in agent_pool:
        agent_pool[request.session_id] = CosmicWorksAIAgent(request.session_id)
    return { "message": agent_pool[request.session_id].run(request.prompt) }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4242, reload=True)
