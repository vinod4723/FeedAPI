import httpx

API_URL = "https://api.open-meteo.com/v1/forecast"

async def fetch_weather(city: str):
    """Fetch weather data from external public API."""
    async with httpx.AsyncClient() as client:
        params = {"latitude": 28.61, "longitude": 77.23, "current_weather": True}  # Example: Delhi
        response = await client.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
