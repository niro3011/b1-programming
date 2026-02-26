from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from user_store import UserStore

app = FastAPI()


store = UserStore("users.txt")



class UserCreate(BaseModel):
    name: str
    email: str



@app.get("/users")
def get_users():
    users = store.load()
    return users



@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User nicht gefunden")
    return user


@app.post("/users")
def create_user(user_data: UserCreate):
    users = store.load()


    if len(users) == 0:
        neue_id = 1
    else:
        hoechste_id = 0
        for user in users:
            if user["id"] > hoechste_id:
                hoechste_id = user["id"]
        neue_id = hoechste_id + 1

    neuer_user = {
        "id": neue_id,
        "name": user_data.name,
        "email": user_data.email
    }

    users.append(neuer_user)
    store.save(users)

    return neuer_user



@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: UserCreate):
    erfolgreich = store.update_user(user_id, {"name": user_data.name, "email": user_data.email})
    if not erfolgreich:
        raise HTTPException(status_code=404, detail="User nicht gefunden")
    return {"message": "User wurde aktualisiert"}


# DELETE /users/{user_id} - User löschen@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    erfolgreich = store.delete_user(user_id)
    if not erfolgreich:
        raise HTTPException(status_code=404, detail="User nicht gefunden")
    return {"message": "User wurde gelöscht"}
