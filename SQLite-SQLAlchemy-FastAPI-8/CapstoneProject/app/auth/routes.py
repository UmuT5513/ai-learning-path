from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from CapstoneProject.app.deps import get_db
from CapstoneProject.app.auth import schemas, service
from CapstoneProject.app.auth.models import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=schemas.UserOut)
def register(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=payload.email, password_hash=service.hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", response_model=schemas.TokenOut)
def login(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not service.verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access, refresh = service.create_tokens(user)
    return {
        "access_token": access,
        "refresh_token": refresh,
        "expires_in": 60 * settings.ACCESS_TTL_MIN
    }
