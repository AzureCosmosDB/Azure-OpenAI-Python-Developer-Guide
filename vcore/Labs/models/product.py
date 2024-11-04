"""
Product model
"""
from typing import List, Optional
from pydantic import BaseModel, Field
from .tag import Tag

class Product(BaseModel):
    """
    The Product class represents a product in the
    Cosmic Works dataset.
    """
    id: str = Field(default=None, alias="_id")
    category_id: str = Field(alias="categoryId")
    category_name: str = Field(alias="categoryName")
    sku: str
    name: str
    description: str
    price: float
    tags: Optional[List[Tag]] = []

    class Config:
        """
        The Config inner class is used to configure the
        behavior of the Pydantic model. In this case,
        the Pydantic model will be able to deserialize
        data by both the field name and the field alias.        
        """
        populate_by_name = True

class ProductList(BaseModel):
    """
    The ProductList class represents a list of products.
    This class is used when deserializing a collection/array
    of products.
    """
    items: List[Product]
