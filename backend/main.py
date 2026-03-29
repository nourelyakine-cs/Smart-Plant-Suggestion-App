from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from routes.plants import router as plants_router

app = FastAPI(
    title="Smart Plant Suggestion API",
    description="Backend for the Smart Plant Suggestion App",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plants_router, prefix="/api")


@app.get("/")
def root():
    return {
        "name": "Smart Plant Suggestion API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "ai_service": os.getenv("AI_SERVICE_URL", "http://localhost:5001")
    }
