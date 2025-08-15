
from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str
    author: str
    year: int

class UserBase(BaseModel):
    name:str
    email:str

class BookCreate(BookBase):
    pass

class UserCreate(UserBase):
    pass


class BookOut(BookBase):
    id: int


class UserOut(UserBase):
    id: int


class BookUpdate(BaseModel):
    title:str|None =  Field(default=None, description="kitap başlığı/ismi")
    author:str|None = Field(default=None, description="yazar ismi/mahlası")
    year:int|None = Field(default=None, description="yayımlanma tarihi")