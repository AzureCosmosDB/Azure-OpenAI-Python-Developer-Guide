from pydantic import BaseModel

# Define the model for a Chat Session response
class ChatSessionResponse(BaseModel):
    session_id: str
    title: str
