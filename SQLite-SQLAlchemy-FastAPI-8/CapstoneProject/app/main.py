from fastapi import FastAPI
from CapstoneProject.app.auth.routes import router as auth_router # auth_router burada .py dosyası

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def root():
    return {"hello": "world"}


