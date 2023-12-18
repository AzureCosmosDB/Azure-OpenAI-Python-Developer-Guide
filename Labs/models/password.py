from pydantic import BaseModel

class Password(BaseModel):
    hash: str
    salt: str