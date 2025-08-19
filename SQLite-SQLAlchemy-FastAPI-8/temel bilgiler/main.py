from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import UserCreate

# diğer dosyalardan
import models
from database import engine, SessionLocal

app = FastAPI()

# veri tabanı oluştur
models.Base.metadata.create_all(bind=engine)

# DB oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# session: Session = Depends(get_db)
@app.post("/user_create")
def create_user(user: UserCreate, session: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# user1 = UserCreate(name="umut",email="umut@gmail.com")
# print(create_user(user1))
