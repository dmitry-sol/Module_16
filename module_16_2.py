from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello, 16_2!"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[
                    int,
                    Path(
                        ge=1,
                        le=100,
                        title="Enter User ID",
                        example=1)
                    ]):
    return {"message": f'Вы вошли как пользователь № {user_id}'}

@app.get("/user/{username}/{age}")
def get_user_info(username: Annotated[
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
                    ]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# uvicorn module_16_2:app --reload