from fastapi import FastAPI
# uvicorn main:app --reload
app = FastAPI()

users= []

@app.get("/")
def read_root():
    return {"Hello": "World", "output":True}

@app.post("/users/")
def add(user: str):
    users.append(user)
    return {"user": user, "users": users, "durum": "kullanıcı eklendi"}

@app.put("/users/{user_id}")
def update(user_id, user):
    if user in users:
        return {"user_id": user_id, "user": user, "users": users}
    else:
        return {"kullanıcı listesinde olan bir kişi ismi girin!"}