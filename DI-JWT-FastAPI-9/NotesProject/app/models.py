import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from base import Base


class Role(str, enum.Enum):

    ADMİN = "admin"
    USER = "user"


class Priority(str, enum.Enum):
    
    URGENT = "urgent"
    MEDIUM = "medium"
    LAZY = "lazy"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)
    notes = relationship("Note", back_populates="owner")

class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User",back_populates="notes")
    

    
    
