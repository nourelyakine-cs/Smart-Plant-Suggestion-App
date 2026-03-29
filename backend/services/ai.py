import httpx
import os

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:5001")


async def get_plants_list():
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"{AI_SERVICE_URL}/api/plants")
        response.raise_for_status()
        return response.json()


async def get_weather_data(city: str):
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"{AI_SERVICE_URL}/api/weather/{city}")
        response.raise_for_status()
        return response.json()


async def get_suggestions(city: str):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{AI_SERVICE_URL}/api/suggest",
            params={"city": city}
        )
        response.raise_for_status()
        return response.json()


async def chat_with_ai(message: str, session_id: str = "default"):
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{AI_SERVICE_URL}/api/chat",
            json={"message": message, "session_id": session_id}
        )
        response.raise_for_status()
        return response.json()
