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
        from_attributes = True  # Pydantic V2 için orm_mode yerine from_attributes


# User schemas
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

class UserCreate(User): # bununla user oluşturacağız, UserInDB ile db ye kaydedeceğiz. böyle yapmamızın sebebi password u hashlenmiş olarak kaydetmek
    password: str

class UserOut(UserInDB):
    id:int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


