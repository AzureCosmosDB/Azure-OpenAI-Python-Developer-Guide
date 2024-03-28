"""
SalesOrderDetail model
"""
from pydantic import BaseModel

class SalesOrderDetail(BaseModel):
    """
    The SalesOrderDetail class represents invoice line items 
    for the Sales Order in the Cosmic Works dataset.
    """
    sku: str
    name: str
    price: float
    quantity: int
