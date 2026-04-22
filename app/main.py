from fastapi import FastAPI
from .routers import stats

app = FastAPI()

app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "This is my root point for RigStastsAPI"}