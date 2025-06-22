from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
