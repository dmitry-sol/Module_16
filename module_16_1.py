from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root() -> str:
    return "Главная Страница"

@app.get("/user/admin")
async def read_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def read_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/")
async def get_user_info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# uvicorn module_16_1:app --reload
