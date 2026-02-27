# Week 15 – Upgrading to SQLite Database

## Projektstruktur

```
week15/
├── main.py         ← FastAPI App mit allen Endpoints
├── user_store.py   ← UserStore Klasse mit SQLite
└── users.db        ← wird automatisch erstellt!
```

## Installation & Starten

### 1. Pakete installieren
```bash
pip install fastapi uvicorn
```

### 2. Server starten
```bash
uvicorn main:app --reload
```

### 3. API testen
Öffne im Browser: http://127.0.0.1:8000/docs  
→ Dort siehst du alle Endpoints und kannst sie direkt ausprobieren!

---

## Alle Endpoints im Überblick

| Methode | URL                  | Beschreibung              |
|---------|----------------------|---------------------------|
| GET     | /users               | Alle User abrufen         |
| GET     | /users/{id}          | Einen User abrufen        |
| POST    | /users               | Neuen User erstellen      |
| PUT     | /users/{id}          | User aktualisieren        |
| DELETE  | /users/{id}          | User löschen              |

---

## Beispiele mit curl

```bash
# Alle User abrufen
curl http://127.0.0.1:8000/users

# Neuen User erstellen
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Max Mustermann", "email": "max@example.com"}'

# User mit ID 1 abrufen
curl http://127.0.0.1:8000/users/1

# User mit ID 1 aktualisieren
curl -X PUT http://127.0.0.1:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Max Neu"}'

# User mit ID 1 löschen
curl -X DELETE http://127.0.0.1:8000/users/1
```

---

## Was macht was?

### user_store.py – die Datenbank-Klasse

| Methode                        | Was sie macht                          |
|--------------------------------|----------------------------------------|
| `__init__(db_path)`            | Speichert den Pfad, ruft init_db auf   |
| `init_db()`                    | Erstellt die Tabelle falls nötig       |
| `load()`                       | Gibt alle User als Liste zurück        |
| `save(user)`                   | Fügt neuen User ein, gibt ID zurück    |
| `find_by_id(user_id)`          | Sucht User per ID, gibt Dict zurück    |
| `update_user(user_id, data)`   | Aktualisiert User, gibt True/False     |
| `delete_user(user_id)`         | Löscht User, gibt True/False zurück    |
