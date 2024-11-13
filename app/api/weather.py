import logging
from fastapi import APIRouter

from app.services.cache_services.redis_cache_service import RedisCacheService
from app.services.weather_service import WeatherService

logger = logging.getLogger("weather_api")

router = APIRouter()


@router.get("/")
async def get_weather(city: str):
    return await WeatherService("http").get(city)
