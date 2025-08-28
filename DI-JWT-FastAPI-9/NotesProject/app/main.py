from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from base import SessionLocal, engine, Base
import models
from sqlalchemy.orm import Session
import schemas
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
import jwt
from settings import settings


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # authprization username ve password ile otomaikt olarak /token endpointi çağrılarak yapılır. yani login sonrası gelen tokeni copy paste yapmaya gerk yok.

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # şifre encyrptleme




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



def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)) -> models.User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    
    user = session.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user


def get_user_by_username(username:str, session: Session):
    return session.query(models.User).filter(models.User.username == username).first()


def create_user(user: schemas.UserCreate, session: Session) -> schemas.UserOut:
    db_user = models.User(username=user.username, hashed_password=hash_password(user.password), role=user.role) 
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt








@app.get("/")
def root():
    return {"ProjectName": "NoteSystem"}



@app.get("/users", response_model=list[schemas.UserOut])
def list_users(session: Session = Depends(get_db)) -> list[models.User]:

    users = session.query(models.User).all()

    return users


@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id:int, session: Session = Depends(get_db)) -> models.User:
    user = session.query(models.User).filter(models.User.id == user_id).first()
    return user


@app.post("/register")
def register(username:str, password:str, session: Session = Depends(get_db)):
    '''inputları db ye kayıt eder'''
    db_user = get_user_by_username(username=username, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail="kullanıcı adı zaten kayıtlı")
    
    username = username
    password = password
    role = models.Role.USER

    user = create_user(schemas.UserCreate(username=username, password=password, role=role), session=session) # models.User döndürür.
    return {"msg": "User created", "username": user.username}


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    '''inputlar db ile eşleşiyorsa token üret'''
    db_user = session.query(models.User).filter(models.User.username == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Yanlış kullanıcı adı ve ya şifre!")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
    


@app.post("/notes")
def create_note(note:schemas.NoteCreate, 
                session : Session = Depends(get_db), 
                current_user: models.User = Depends(get_current_user)):
    
    
    db_note = models.Note(title=note.title, content=note.content, owner_id=current_user.id)

    session.add(db_note)
    session.commit()
    session.refresh(db_note)

    return {"INFO":"note added", "note":f"{db_note.content}"}


@app.get("/notes",response_model=list[schemas.NoteOut])
def list_notes(session:Session = Depends(get_db), current_user: models.User = Depends(get_current_user))->list[models.Note]:

    notes = session.query(models.Note).filter(models.Note.owner_id == current_user.id).all()

    return notes


@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
def get_note(note_id:int, session: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)) -> models.Note:
    
    # current user ın ilgili notunu getir
    note = session.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="note bulunamadı ve ya üzerinize olmayan bir not id si girdinz")

    return note


@app.put("/notes/{note_id}")
def update_not(note_id:int, note: schemas.NoteCreate ,session: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_note = session.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="note bulunamadı ve ya üzerinize olmayan bir not id si girdinz")

    db_note.title = note.title  # type: ignore
    db_note.content = note.content  # type: ignore
    session.commit()
    session.refresh(db_note)
    return {"INFO": "note updated", "note": db_note.title}

@app.delete("/notes/{note_id}")
def delete_note(note_id:int, session:Session = Depends(get_db), current_user:models.User = Depends(get_current_user)):
    db_note = session.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="note bulunamadı ve ya üzerinize olmayan bir not id si girdinz")
    
    session.delete(db_note)
    session.commit()

    return {"INFO": "note deleted", "deleted_note_id": note_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


    