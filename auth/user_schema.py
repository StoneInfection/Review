from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    role: str


class UserSchema(BaseModel):
    id: int
    name: str
    role: str


class UserRegistration(BaseModel):
    name: str
    password: str
