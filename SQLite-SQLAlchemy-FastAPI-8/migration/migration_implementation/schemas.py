from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    name:str
    email:str
    age:int

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id:int