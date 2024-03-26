"""
AIRequest model
"""
from pydantic import BaseModel

class AIRequest(BaseModel):
    """
    AIRequest model encapsulates the session_id
    and incoming user prompt for the AI agent
    to respond to.
    """
    session_id: str
    prompt: str
