from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    DATABASE_URL: str | None = 'sqlite:///app.db'
    JWT_SECRET: str | None = 'super_secret_key_123'
    JWT_ALG: str = "HS256"
    ACCESS_TTL_MIN: int = 15
    REFRESH_TTL_DAYS: int = 7

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
