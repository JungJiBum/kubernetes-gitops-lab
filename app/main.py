import os
from fastapi import FastAPI

app = FastAPI(title="Kubernetes GitOps Lab")

APP_VERSION = os.getenv("APP_VERSION", "v1")
APP_ENV = os.getenv("APP_ENV", "local")

@app.get("/")
def root():
    return {
        "message": "Kubernetes GitOps Lab",
        "environment": APP_ENV,
        "version": APP_VERSION,
    }


@app.get("/health/live")
def live():
    return {"status": "alive"}


@app.get("/health/ready")
def ready():
    return {"status": "ready"}


@app.get("/version")
def version():
    return {"version": APP_VERSION}