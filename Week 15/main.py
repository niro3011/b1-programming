from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from user_store import UserStore

app = FastAPI()


store = UserStore("users.db")

class UserCreate(BaseModel):
    name:  str
    email: str

class UserUpdate(BaseModel):
    name:  Optional[str] = None
    email: Optional[str] = None


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


@app.post("/users", status_code=201)
def create_user(user_data: UserCreate):

    new_user = {
        "name":  user_data.name,
        "email": user_data.email
    }

    new_id = store.save(new_user)

    return store.find_by_id(new_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    updated_data = user_data.model_dump(exclude_none=True)

    if not updated_data:
        raise HTTPException(status_code=400, detail="Keine Daten zum Aktualisieren angegeben")

    success = store.update_user(user_id, updated_data)

    if not success:
        raise HTTPException(status_code=404, detail="User nicht gefunden")

    return store.find_by_id(user_id)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User nicht gefunden")

    return {"message": f"User mit ID {user_id} wurde erfolgreich gelöscht"}
