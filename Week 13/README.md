# Week 13 – FastAPI User Management

## Schritt-für-Schritt Setup

```bash
# 1. In den Projektordner wechseln
cd week13

# 2. Virtual Environment erstellen
python3 -m venv venv

# 3. Virtual Environment aktivieren
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# 4. Pakete installieren
pip install fastapi uvicorn

# 5. Server starten  ← immer aus dem week13/ Ordner heraus!
uvicorn main:app --reload
```

## Endpoints

| Methode | URL                        | Beschreibung          |
|---------|----------------------------|-----------------------|
| GET     | /                          | Health Check          |
| GET     | /health                    | Detaillierter Status  |
| POST    | /users/                    | User erstellen        |
| GET     | /users/                    | Alle User             |
| GET     | /users/search?q=Max        | User nach Name suchen |
| GET     | /users/{id}                | Einzelner User        |
| PUT     | /users/{id}                | User aktualisieren    |
| DELETE  | /users/{id}                | User löschen          |

## Testen

Einfach im Browser öffnen:  
👉 http://127.0.0.1:8000/docs  ← Swagger UI, alles anklickbar!

## Dateistruktur

```
week13/
├── main.py          ← Einstiegspunkt, App starten
├── schema.py        ← Datenmodelle (User, UserCreate)
├── users.txt        ← Datenbank (JSON-Datei)
├── README.md        ← Diese Anleitung
├── routes/
│   ├── __init__.py  ← Pflichtdatei (darf leer sein)
│   └── users.py     ← Alle /users Endpunkte
└── venv/            ← Virtual Environment (nicht in Git!)
```

## Häufige Fehler

**ModuleNotFoundError: No module named 'schema'**  
→ Server **nicht** aus dem routes/ Ordner starten, sondern aus week13/  
→ Richtig: `cd week13 && uvicorn main:app --reload`

**Address already in use**  
→ Port 8000 ist belegt: `uvicorn main:app --reload --port 8001`
