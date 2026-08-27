import httpx
from app.config import OPEN_WEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5"

async def get_current_weather(city: str):
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid" : OPEN_WEATHER_API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.json()

async def get_forecast(city: str):
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid" : OPEN_WEATHER_API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.json()
