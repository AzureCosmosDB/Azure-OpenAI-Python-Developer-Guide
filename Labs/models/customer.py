"""
Customer and CustomerList models
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from .address import Address
from .password import Password

class Customer(BaseModel):
    """
    The Customer class represents a customer in the
    Cosmic Works dataset.

    The alias feelds are used to map the dataset
    field names to the pythonic property names.
    """
    id: str = Field(alias="_id")
    customer_id: str = Field(alias="customerId")
    title: Optional[str]
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email_address: str = Field(alias="emailAddress")
    phone_number: str = Field(alias="phoneNumber")
    creation_date: datetime = Field(alias="creationDate")
    addresses: List[Address]
    password: Password
    sales_order_count: int = Field(alias="salesOrderCount")

    class Config:
        """
        The Config inner class is used to configure the 
        behavior of the Pydantic model. In this case, 
        the Pydantic model will be able to deserialize
        data by both the field name and the field alias.
        """
        populate_by_name = True

class CustomerList(BaseModel):
    """
    The CustomerList class represents a list of customers.
    This class is used when deserializing a collection/array
    of customers.
    """
    items: List[Customer]
