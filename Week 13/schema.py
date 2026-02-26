from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    age: int


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
