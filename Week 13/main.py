from fastapi import FastAPI
from routes import users

app = FastAPI(
    title="User Management API",
    description="FastAPI Backend für die Verwaltung von Usern",
    version="1.0.0",
)


app.include_router(users.router, prefix="/users", tags=["Users"])


@app.get("/", tags=["Health"])
def root():
    return {"status": "healthy", "message": "API läuft!"}


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "message": "Alles in Ordnung!",
    }
