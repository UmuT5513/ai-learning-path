from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseUser(BaseModel):
    username:str
    email: EmailStr
    age: int
    full_name: Optional[str] = None

class UserIn(BaseUser):
    password: str


class ItemBaser(BaseModel):
    name: str
    description: Optional[str] = None
    in_stock: bool = True
    price:float
    

class ItemCreate(ItemBaser):
    pass

class Item(ItemBaser):
    id: int
