"""
SalesOrder model
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from .sales_order_detail import SalesOrderDetail

class SalesOrder(BaseModel):
    """
    The SalesOrder class represents a sales order in the
    Cosmic Works dataset.
    """
    id: str = Field(alias="_id")
    customer_id: str = Field(alias="customerId")
    order_date: datetime = Field(alias="orderDate")
    ship_date: datetime = Field(alias="shipDate")
    details: List[SalesOrderDetail]

    class Config:
        """
        The Config inner class is used to configure the
        behavior of the Pydantic model. In this case,
        the Pydantic model will be able to deserialize
        data by both the field name and the field alias.
        """
        populate_by_name = True

class SalesOrderList(BaseModel):
    """
    The SalesOrderList class represents a list of sales orders.

    This class is used when deserializing a collection/array
    of sales orders.
    """
    items: List[SalesOrder]
