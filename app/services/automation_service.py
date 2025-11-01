import asyncio
from app.utils.helpers import log_message
from automation.api_caller import fetch_weather

async def get_weather_data(city: str):
    """Async function to fetch external data."""
    log_message(f"Fetching weather data for {city}")
    data = await fetch_weather(city)
    return data

def trigger_daily_job():
    """Example: simulate automation like sending reports or scraping."""
    log_message("Daily job started.")
    # Do your automation logic here
    return {"message": "Daily job completed successfully"}
