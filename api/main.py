from fastapi import FastAPI
from routes import users, auth, orders

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(orders.router)
