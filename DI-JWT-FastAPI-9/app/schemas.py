from pydantic import BaseModel, Field
from datetime import datetime


NOW = datetime.now()


# Log schemas
class LogBase(BaseModel):
    message:str
    created_at:datetime = Field(default_factory=NOW)


class LogCreate(LogBase):
    pass
    


class LogOut(LogBase):
    id:int

    class Config:
        orm_mode = True


# User schemas
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

class UserCreate(User): # bununla user oluşturacağız, UserInDB ile db ye kaydedeceğiz.
    password: str

class UserOut(UserInDB):
    id:int


