from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Папка для хранения шаблонов

users: List['User'] = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=RedirectResponse)
async def get_main_page():
    return RedirectResponse(url="/users", status_code=303)

@app.get("/users")
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/add_user")
async def show_add_user_form(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})

@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post("/user", response_model=User)
async def add_user(request: Request, username: str = Form(...), age: int = Form(...)):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "user": new_user})

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def edit_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

# uvicorn module_16_5:app --reload