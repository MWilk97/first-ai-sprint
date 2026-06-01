from fastapi import FastAPI
from app.db import engine, Base
from app.models.user import User

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}
