from pydantic import BaseModel, Field
import models

class User(BaseModel):

    id:str
    username:str
    #password:str
    role:models.Role

    


class UserOut(User):

    class Config:
        from_attributes = True
    


class Note(BaseModel):

    title:str
    content:str


class NoteCreate(Note):
    pass


class NoteOut(Note):
    id:int
    owner_id:int

    class Config:
        from_attributes = True