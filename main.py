from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = []  # Lista para almacenar los usuarios temporalmente

@app.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "Usuario guardado correctamente", "user": user}

@app.get("/users/")
def get_users():
    return {"users": users}

@app.get("/users-nuevo/")
def get_users():
    return {"users_2": users}
