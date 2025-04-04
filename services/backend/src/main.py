from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import os 
from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join("database", ".env"))

print('secret')
print(os.environ.get("SECRET_KEY"))

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

"""
import 'from src.routes import users, notes' must be after 'Tortoise.init_models'
why?
https://stackoverflow.com/questions/65531387/tortoise-orm-for-python-no-returns-relations-of-entities-pyndantic-fastapi
"""
from src.routes import users, notes

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://tsadimas-vue.ddns.net",
    "https://tsadimas-vue.ddns.net",
    "http://tsadimas-fastapi.ddns.net",
    "https://tsadimas-fastapi.ddns.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE","OPTIONS"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


print(os.environ.get("DATABASE_URL"))

@app.get("/")
def home():
    return "Hello, World!"
