from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from base import SessionLocal, engine, Base
import models
from sqlalchemy.orm import Session


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# veri tabanı oluştur
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(pwd:str) -> str:
    return pwd_context.hash(pwd)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# şimdilik token == username !
def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)) -> models.User:
    user = session.query(models.User).filter(models.User.username == token).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user


def require_role(required: models.Role):
    def checker(current_user: models.User = Depends(get_current_user)):
        if str(current_user.role) != str(required):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="FORBIDDEN")
        return current_user
    return checker


def owner_or_admin_door(note_id:int, current_user: models.User = Depends(get_current_user), session:Session = Depends(get_db)):
    note = session.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
    if str(note.owner_id) != str(current_user.id):
        raise HTTPException(status_code=403, detail="FORBIDDEN")
    return note
    