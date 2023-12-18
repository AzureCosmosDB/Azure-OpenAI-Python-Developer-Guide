from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .sales_order_detail import SalesOrderDetail

class SalesOrder(BaseModel):
    id: str = Field(alias="_id")
    customer_id: str = Field(alias="customerId")
    order_date: datetime = Field(alias="orderDate")
    ship_date: datetime = Field(alias="shipDate")
    details: List[SalesOrderDetail]
   
    class Config:
        populate_by_name = True

class SalesOrderList(BaseModel):
    items: List[SalesOrder]
