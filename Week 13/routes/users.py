import json
import os
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from schema import User, UserCreate

router = APIRouter()


USERS_FILE = "users.txt"


def read_users() -> List[dict]:
    """Liest alle User aus der users.txt Datei."""
    if not os.path.exists(USERS_FILE):

        return []

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if content == "" or content == "[]":
        return []

    return json.loads(content)


def write_users(users: List[dict]) -> None:
    """Schreibt alle User in die users.txt Datei."""
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)


def get_next_id() -> int:
    """Gibt die nächste freie ID zurück."""
    users = read_users()

    if len(users) == 0:
        return 1

    max_id = 0
    for user in users:
        if user["id"] > max_id:
            max_id = user["id"]

    return max_id + 1

@router.post("/", response_model=User, status_code=201)
def create_user(user_data: UserCreate):
    """Erstellt einen neuen User."""
    users = read_users()

    new_user = {
        "id": get_next_id(),
        "name": user_data.name,
        "email": user_data.email,
        "age": user_data.age,
    }

    users.append(new_user)
    write_users(users)

    return new_user


@router.get("/", response_model=List[User])
def get_all_users():
    """Gibt alle User zurück."""
    users = read_users()
    return users


@router.get("/search", response_model=List[User])
def search_users(q: str):
    """Sucht User nach Name (Groß/Kleinschreibung wird ignoriert)."""
    users = read_users()

    results = []
    for user in users:
        if q.lower() in user["name"].lower():
            results.append(user)

    return results


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    """Gibt einen einzelnen User anhand der ID zurück."""
    users = read_users()

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail=f"User mit ID {user_id} nicht gefunden")


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserCreate):
    """Aktualisiert einen bestehenden User."""
    users = read_users()

    for i in range(len(users)):
        if users[i]["id"] == user_id:
            users[i]["name"] = user_data.name
            users[i]["email"] = user_data.email
            users[i]["age"] = user_data.age

            updated_user = users[i]
            write_users(users)

            return updated_user

    raise HTTPException(status_code=404, detail=f"User mit ID {user_id} nicht gefunden")


@router.delete("/{user_id}")
def delete_user(user_id: int):
    """Löscht einen User anhand der ID."""
    users = read_users()

    new_list = []
    found = False

    for user in users:
        if user["id"] == user_id:
            found = True  
            new_list.append(user)

    if not found:
        raise HTTPException(status_code=404, detail=f"User mit ID {user_id} nicht gefunden")

    write_users(new_list)

    return {"message": f"User mit ID {user_id} wurde erfolgreich gelöscht"}
