from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from .address import Address
from .password import Password

class Customer(BaseModel):
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
        populate_by_name = True

class CustomerList(BaseModel):
    items: List[Customer]