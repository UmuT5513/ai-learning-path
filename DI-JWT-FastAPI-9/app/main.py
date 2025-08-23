from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import models
from base import engine, SessionLocal, DATABASE_URL
import schemas
from sqlalchemy.orm.session import Session


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
# 2 bölümden oluşur. 1: create_user gibi db ile user işlemleri. 2: doğrulama işlemleri

@app.post("/user", response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, session: Session = Depends(get_db)):
    db_user = models.User(**user, password=fake_hash_password(user.hashed_password)) # id yi otomatik olarak veriyor
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_user( username: str, session: Session = Depends(get_db)):
    db = session.query(models.User).all()
    if username in db:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)
    
# En güvensiz YÖNTEM 1:
def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(username=token, session=Depends(get_db))
    return user

# YÖNTEM 2:
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)])->schemas.UserOut:
    # dikkat! token i Depends ile alıyoruz. Depends str döndürür.
    user = fake_decode_token(token)
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


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_db)):
    user = session.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = schemas.UserInDB(**user)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}



@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[schemas.UserOut, Depends(get_current_active_user)],
):
    return current_user




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
