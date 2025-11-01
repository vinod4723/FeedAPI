from fastapi import APIRouter, Depends
from flask import session
from sqlalchemy.orm import Session, Query

from app.services.automation_service import get_weather_data, trigger_daily_job
from app.services.employee_service import get_all_employees
from app.db.database import get_db
router = APIRouter()

@router.get("/weather/{city}")
async def weather(city: str):
    """Example endpoint to fetch weather data using an external API."""
    data = await get_weather_data(city)
    return {"city": city, "data": data}

@router.post("/run-job")
def run_job():
    """Trigger a manual automation job."""
    result = trigger_daily_job()
    return {"status": "Job triggered", "result": result}
