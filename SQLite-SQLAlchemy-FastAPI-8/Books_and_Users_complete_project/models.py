from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from database import Base



class User(Base):


    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    books = relationship("Book", back_populates="owner") # child class name


class Book(Base):


    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

    user_id = Column(Integer, ForeignKey("User.id")) # parent classın table_name i = User
    owner = relationship("User", back_populates="books") # back_populates parent class daki relationships dir.