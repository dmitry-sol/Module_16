from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def read_root() -> str:
    return "Главная страница 16_2"

@app.get("/user/admin")
async def read_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[
                    int,
                    Path(
                        ge=1,
                        le=100,
                        title="Enter User ID",
                        example=1)
                    ]) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[
                    str,
                    Path(
                        min_length=5,
                        max_length=20,
                        title="Enter username",
                        example='UrbanUser')
                    ],
                  age: Annotated[
                    int,
                    Path(
                        ge=18,
                        le=120,
                        title="Enter age",
                        example=24)
                    ]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# uvicorn module_16_2:app --reload
