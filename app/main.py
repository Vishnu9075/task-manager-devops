from fastapi import FastAPI
from app.db import engine, Base
from app.models import Task  # ensures model metadata is registered
from sqlalchemy import text
import time

app = FastAPI(title="Task Manager DevOps")


@app.on_event("startup")
def startup():
    max_retries = 10
    retry_delay = 3

    for attempt in range(max_retries):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            Base.metadata.create_all(bind=engine)
            print("Database connected and tables created.")
            return
        except Exception as e:
            print(f"Database not ready yet (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(retry_delay)

    raise RuntimeError("Could not connect to database after multiple retries.")


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}