"""
Tag model
"""
from pydantic import BaseModel, Field

class Tag(BaseModel):
    """
    The Tag class represents a tag in the
    Cosmic Works dataset.

    Tags are metadata associated with a product.
    """
    id: str = Field(default=None, alias="_id")
    name: str

    class Config:
        """
        The Config inner class is used to configure the
        behavior of the Pydantic model. In this case,
        the Pydantic model will be able to deserialize
        data by both the field name and the field alias.
        """
        populate_by_name = True
