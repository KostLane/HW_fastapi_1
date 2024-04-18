# Задание №3, 4, 5
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST, PUT, DELETE запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST, PUT, DELETE).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []

@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return {"message": "Пользователь успешно добавлен"}

@app.put("/user/{id}")
async def update_user(id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.id == id:
            users[index] = user
            return {"message": "Успешное изменение"}
    raise HTTPException(status_code=404, detail="Поьзователь не найден")

@app.delete("/user/{id}")
async def delete_user(id: int):
    for index, existing_user in enumerate(users):
        if existing_user.id == id:
            users.pop(index)
            return {"message": "Пользователь успешно удален"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)