from fastapi import FastAPI, Request
from datetime import datetime, timezone
import platform
import time

START_TIME = time.time()

app = FastAPI(title="Health Check API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "API is running", "docs": "/docs"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
    }


@app.get("/ping")
def ping():
    return {"pong": True}


@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    return {
        "received": body,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info")
def info():
    return {
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "hostname": platform.node(),
    }
