from fastapi import FastAPI
from app.routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}