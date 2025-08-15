from sqlalchemy import Integer, String, Column
from database import Base


class Book(Base):


    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)


class User(Base):


    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)