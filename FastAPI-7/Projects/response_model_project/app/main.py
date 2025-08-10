from fastapi import FastAPI, HTTPException
from schemas import UserIn, BaseUser, ItemCreate, Item
from utils import fake_hash_password

app = FastAPI()

fake_user_db={}
fake_item_db=[] #item lar dict olarak tutulur
item_id_counter=1

@app.post("/users", response_model=BaseUser, response_model_exclude_none=True)
def create_user(user: UserIn)->BaseUser:
    dict = user.model_dump()
    dict.update({"password": fake_hash_password(user.password)})
    fake_user_db[user.username] = dict
    return dict

@app.get("/users/{username}")
def read_user(username:str):
    user = next(filter(lambda u: u["username"] == username, fake_user_db.values()), None)
    return user

@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate)-> Item:
    global item_id_counter
    item = item.model_dump()
    item["id"] = item_id_counter
    item_id_counter+=1
    fake_item_db.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id:str)->Item:
    item = next(filter(lambda i: i["id"] == item_id, fake_item_db), None)
    return item

@app.get("/items/")
def read_items():
    return fake_item_db

@app.put("/items/{item_id}")
def update_item(item_id:str, updated_item:ItemCreate)->Item:
    for i in fake_item_db:
        if i["id"] == item_id:
            updated_dict = updated_item.model_dump()
            updated_dict["id"] = item_id
            fake_item_db[item_id] = updated_dict
            return updated_dict
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id:str)->Item:
    for index, item in fake_item_db:
        if item["id"] == item_id:
            del fake_item_db[index]
            return {"message": "Item deleted"}
        raise HTTPException(status_code=404, detail="Item not found")
        

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)