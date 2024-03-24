from fastapi import FastAPI
from db import models
from db.config import engine
from routes import users, posts

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)


#uvicorn main:app --host 127.0.0.1 --port 8080
