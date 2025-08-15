from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./books.db"
DATABASE_URL_users = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_users = create_engine(DATABASE_URL_users, connect_args={"check_same_thread": False})
SessionLocal_users = sessionmaker(autocommit=False, autoflush=False, bind=engine_users)

Base = declarative_base()


