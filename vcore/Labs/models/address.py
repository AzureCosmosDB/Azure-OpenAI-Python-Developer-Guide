"""
Address model
"""
from pydantic import BaseModel, Field

class Address(BaseModel):
    """
    The Address class represents the structure of
    an address in the Cosmic Works dataset.
    """
    address_line_1: str = Field(alias="addressLine1")
    address_line_2: str = Field(alias="addressLine2")
    city: str
    state: str
    country: str
    zip_code: str = Field(alias="zipCode")
