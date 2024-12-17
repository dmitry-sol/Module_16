from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users: List['User'] = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def read_root() -> str:
    return 'Главная страница модуля 16_4'

@app.get('/users', response_model=List[User])
async def get_users():
    return users

@app.post('/user/{username}/{age}', response_model=User)
async def add_user(username: str, age: int):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def edit_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='Имя не найдено')

@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail='Имя не найдено')

# uvicorn module_16_4:app --reload
