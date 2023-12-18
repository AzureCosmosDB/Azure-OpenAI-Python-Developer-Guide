from pydantic import BaseModel, Field
from typing import List
from .tag import Tag

class Product(BaseModel):
    id: str = Field(alias="_id")
    categoryId: str
    categoryName: str
    sku: str
    name: str
    description: str
    price: float
    tags: List[Tag]

    class Config:
        populate_by_name = True

class ProductList(BaseModel):
    items: List[Product]
