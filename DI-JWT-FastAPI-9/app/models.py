from base import Base # declarative_base()
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean

class Log(Base):

    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())

    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)