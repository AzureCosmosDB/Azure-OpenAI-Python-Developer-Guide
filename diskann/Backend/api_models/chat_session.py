from pydantic import BaseModel, Field
from typing import List

class ChatSession(BaseModel):
    id: str # The session ID
    title: str # The title of the chat session
    history: List[dict] = Field(default_factory=list) # The chat history
