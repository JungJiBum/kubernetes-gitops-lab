import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/web", response_class=HTMLResponse)
def web():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Kubernetes GitOps Lab</title>
        <style>
            body {
                background: #101827;
                color: white;
                font-family: sans-serif;
                display: grid;
                place-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                padding: 48px;
                border: 1px solid #334155;
                border-radius: 20px;
                text-align: center;
            }
            h1 { color: #38bdf8; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Kubernetes GitOps Lab</h1>
            <h2>CI/CD Deployment Test</h2>
            <p>FastAPI + Docker + GitHub Actions + Argo CD</p>
            <p>DEV Deployment Verification</p>
        </div>
    </body>
    </html>
    """