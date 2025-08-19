from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class User(Base):
   __tablename__ = "users"
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)
   email = Column(String, unique=True, index=True)
   transaction_date = Column(DateTime, nullable=True)
   age:int = Column(Integer)