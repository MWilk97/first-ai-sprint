from fastapi import FastAPI
from app.db import engine, Base

app = FastAPI()

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}