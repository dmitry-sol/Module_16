from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello, World!"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"message": f'Вы вошли как пользователь № {user_id}'}

@app.get("/user/")
def get_user_info(username: str, age: str):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# uvicorn module_16_1:app --reload
