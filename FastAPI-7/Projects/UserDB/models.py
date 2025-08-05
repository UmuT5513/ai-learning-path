from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name:str
    age:int
    email: EmailStr

class UserOut(User):
    id:int