from fastapi import FastAPI
from app.routers import health, aws, security

app = FastAPI(
    title="Cloud Security Monitoring Dashboard",
    version="1.0.0",
    description="Backend API for Cloud Security Monitoring Dashboard"
)

app.include_router(health.router)
app.include_router(aws.router)
app.include_router(security.router)

@app.get("/")
def root():
    return {
        "application": "Cloud Security Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }
