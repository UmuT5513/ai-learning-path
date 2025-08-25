from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import models
from base import engine, SessionLocal, DATABASE_URL
import schemas
from sqlalchemy.orm.session import Session
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone # create_acces_token de kullanıldı
from dotenv import load_dotenv
from config import settings # .env dosyasından verileri almak için
from passlib.context import CryptContext # pwd_context

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


auto_id = 1

app=FastAPI()


# veri tabanı oluştur
models.Base.metadata.create_all(bind=engine)


# DB oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@app.get("/")
def root():
    return {"message":"DJ_JWT_FASTAPI_9"}

# LOG bölümü - API lar içerir
@app.post("/log", response_model = schemas.LogOut)
def create_log(message:str, session: Session = Depends(get_db)) -> schemas.LogOut:
    logg = models.Log(message=message) #id için sqlalchemy oto id veriyor, created_at zaten now olarak atanıyor
    session.add(logg)
    session.commit()
    session.refresh(logg)
   
    return logg



@app.get("/logs/{log_id}", response_model = schemas.LogOut)
def get_log(log_id:int, session: Session = Depends(get_db))-> schemas.LogOut:

    log = session.query(models.Log).filter(models.Log.id == log_id).first()
    
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    
    return log



@app.get("/logs", response_model=list[schemas.LogOut])
def getlogs(session: Session = Depends(get_db)) -> list[schemas.LogOut]:
    
    logs = session.query(models.Log).all()
    
    return logs



@app.get("/ping") # get kullandık çünkü amacımız db yi test etmek, log kaydetmek değil.
def ping(session: Session = Depends(get_db)):
    create_log(message="ping atıldı!", session=session)
    return {"message":"pong"}

# USER BÖLÜMÜ - API lar ve fonsiyonlar içerir


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)





def create_user(username:str,email:str,full_name:str,password:str, session: Session):
    db_user = models.User(username=username, email=email, full_name=full_name, hashed_password=get_password_hash(password))
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user






def get_user_by_username(username: str, session:Session)->schemas.UserOut:
    db_user = session.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="db de user bulunamadı")
    
    return schemas.UserOut(id=db_user.id, 
                           username=db_user.username, 
                           email=db_user.email, 
                           full_name=db_user.full_name, 
                           hashed_password=db_user.hashed_password, 
                           disabled=db_user.disabled)
    
def check_user_exists(username: str, session: Session) -> bool:
    db_user = session.query(models.User).filter(models.User.username == username).first()
    return db_user is not None

@app.post("/register")
def register(username:str, email:str, full_name:str,password:str, session:Session = Depends(get_db)):
    db_user = check_user_exists(username=username, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail="Kullanıcı zaten var")
    user = create_user(username=username, email=email, full_name=full_name, password=password, session=session)
    return {"msg": "User created", "username": user.username}

def authenticate_user(session:Session, username: str, password: str):
    user = get_user_by_username(username, session)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# En güvensiz YÖNTEM:
def fake_decode_token(token, session:Session) -> schemas.UserOut:
    # This doesn't provide any security at all
    # Check the next version --> JWT ile Auth2
    user = get_user_by_username(username=token, session=session)
    return user

# güvenli yöntem:
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session = Depends(get_db))->schemas.UserOut:
    # dikkat! token i Depends ile alıyoruz. Depends str döndürür.

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    
    user = get_user_by_username(username=token_data.username, session=session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# aktif userı almak
async def get_current_active_user(
    current_user: Annotated[schemas.UserOut, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user





# JWT access token ile dogrulama
@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_db)) -> schemas.Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")



@app.get("/users/me", response_model=schemas.UserOut)
async def read_users_me(
    current_user: Annotated[schemas.UserOut, Depends(get_current_active_user)]):
    return current_user


@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"msg": "You are inside protected area!", "username": current_user.username}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
