from fastapi import FastAPI, HTTPException
from models import User, UserOut

app = FastAPI()

user_db: list[UserOut] = [
    UserOut(id=1, name="Hasan", age=25, email="hasan@example.com"),
    UserOut(id=2, name="Han", age=12, email="han@example.com"),
    UserOut(id=3, name="Mahmut", age=45, email="mahmut@example.com"),
    UserOut(id=4, name="Can", age=5, email="can@example.com"),
]
@app.get("/", response_model=list[UserOut])
def get_users():
    return user_db

@app.get("/check")
def check_user():
    cikti_dict={}
    for i,user in enumerate(user_db):
        user_dict = user.model_dump()
        user_dict.update({"durum": True if user.age > 20 else False})
        cikti_dict[f"{i}"] = user_dict
    return {"output": cikti_dict}


@app.post("/users", response_model=UserOut)
def create_user(user: User):
    # email kontrolü
    if any(u for u in user_db if u.email == user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_id = user_db[-1].id + 1 if user_db else 1
    new_user = UserOut(id=new_id, **user.model_dump())
    user_db.append(new_user)
    return new_user


@app.put("/users/{user_id}", response_model=UserOut)
def update(user_id: int, user: User):
    item = next(filter(lambda u: u.id == user_id, user_db), None)
    if item:
        item.name = user.name
        item.age = user.age
        item.email = user.email
        return item
    
@app.delete("/users/{user_id}")
def delete(user_id:int):
    deleted = next(filter(lambda u: u.id == user_id, user_db), None)
    if deleted:
        user_db.pop(deleted.id - 1)
        return deleted
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    