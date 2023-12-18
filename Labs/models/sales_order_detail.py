from pydantic import BaseModel

class SalesOrderDetail(BaseModel):
    sku: str
    name: str
    price: float
    quantity: int