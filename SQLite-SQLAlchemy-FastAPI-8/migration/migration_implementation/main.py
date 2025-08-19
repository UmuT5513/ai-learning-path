from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

# Import models BEFORE creating tables
import models
from database import engine, SessionLocal
from schemas import UserCreate, UserOut

app = FastAPI()

# Debug: Print all tables before creation
print("Tables before creation:", models.Base.metadata.tables.keys())

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Debug: Print all tables after creation
print("Tables after creation:", models.Base.metadata.tables.keys())

# Debug: Inspect the database
from sqlalchemy import inspect

inspector = inspect(engine)
print("Actual tables in database:", inspector.get_table_names())


# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user_create", response_model=UserOut)
def create_user(user: UserCreate, session: Session = Depends(get_db)):
    # Check if user with email already exists
    existing_user = session.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users")
def get_users(session: Session = Depends(get_db)):
    users = session.query(models.User).all()
    return users







