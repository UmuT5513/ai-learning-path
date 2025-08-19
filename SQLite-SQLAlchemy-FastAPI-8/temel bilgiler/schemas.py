from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    name:str
    email:str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id:int