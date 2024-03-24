from fastapi import FastAPI
from db import models
from db.config import engine
from routes import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)

