from fastapi import FastAPI
from .routes import users

app = FastAPI()

app.add_api_route(users.router)
