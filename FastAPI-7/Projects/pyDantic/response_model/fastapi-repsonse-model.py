from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Veri modeli (response model)
class UserResponse(BaseModel):
    username: str
    email: str

# Endpoint
@app.get("/user", response_model=UserResponse)
async def get_user():
    return {
        "username": "kazloo",
        "email": "kazloo@example.com",
        "password": "süpergizlişifre"  # Bu alan response modelde yok, dönmez!
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




