from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.ai import get_suggestions, chat_with_ai, get_plants_list, get_weather_data

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


@router.get("/plants")
async def list_plants():
    """Get all available plants"""
    try:
        return await get_plants_list()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")


@router.get("/weather/{city}")
async def get_weather(city: str):
    """Get weather data for a city"""
    try:
        return await get_weather_data(city)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Weather service unavailable: {str(e)}")


@router.get("/suggest")
async def suggest_plants(city: str = Query(..., description="City name")):
    """Get plant suggestions matched to city weather"""
    try:
        return await get_suggestions(city)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")


@router.post("/chat")
async def chat(request: ChatRequest):
    """Chat with the AI gardening assistant"""
    try:
        return await chat_with_ai(request.message, request.session_id)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")
