from pydantic import BaseModel, Field
import models

class UserBase(BaseModel):

    username:str
    role:models.Role


class UserCreate(UserBase):

    password:str

    


class UserOut(UserBase):

    id:int

    class Config:
        from_attributes = True
    


class NoteBase(BaseModel):

    title:str
    content:str


class NoteCreate(NoteBase):
    pass


class NoteOut(NoteBase):
    id:int
    owner_id:int
    

    class Config:
        from_attributes = True