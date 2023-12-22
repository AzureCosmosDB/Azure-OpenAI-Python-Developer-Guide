"""
Password model
"""
from pydantic import BaseModel

class Password(BaseModel):
    """
    The Password class represents the structure of
    a password in the Cosmic Works dataset.
    """
    hash: str
    salt: str
