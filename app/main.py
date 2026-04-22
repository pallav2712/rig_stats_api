from fastapi import FastAPI

from app.routers import battery, processes, usage
from .routers import stats

app = FastAPI()

app.include_router(stats.router)
app.include_router(usage.router)
app.include_router(battery.router)
app.include_router(processes.router)


@app.get("/")
def root():
    return {"message": "This is my root point for RigStastsAPI"}