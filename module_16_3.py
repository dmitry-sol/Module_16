from fastapi import FastAPI, HTTPException

app = FastAPI()
users = {'1': 'Имя: Example, Возраст: 18'}

@app.get('/')
async def read_root() -> str:
    return 'Главная страница модуля 16_3'

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int):
    new_id = str(int(max(users, key=int)) + 1) if users else '1'
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {new_id} is updated'

@app.put('/user/{user_id}/{username}/{age}')
async def edit_user(user_id: int, username: str, age: int):
    user_id_str = str(user_id)
    if user_id_str in users:
        users[user_id_str] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id_str} is updated'
    raise HTTPException(status_code=404, detail='Имя не найдено')

@app.delete('/user/{user_id}/')
async def delete_user(user_id: int):
    user_id_str = str(user_id)
    if user_id_str in users:
        del users[user_id_str]
        return f'The user {user_id_str} is deleted'
    raise HTTPException(status_code=404, detail='Имя не найдено')

# uvicorn module_16_3:app --reload
