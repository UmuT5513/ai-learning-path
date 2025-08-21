from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from CapstoneProject.app.config import settings
from CapstoneProject.app.auth.models import User
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALG)

def create_tokens(user: User):
    access = create_token(
        {"sub": str(user.id), "ver": user.token_version},
        timedelta(minutes=settings.ACCESS_TTL_MIN),
    )
    refresh = create_token(
        {"sub": str(user.id), "ver": user.token_version, "type": "refresh"},
        timedelta(days=settings.REFRESH_TTL_DAYS),
    )
    return access, refresh
