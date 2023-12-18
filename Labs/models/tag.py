from pydantic import BaseModel, Field
class Tag(BaseModel):
    id: str = Field(alias="_id")
    name: str

    class Config:
        populate_by_name = True