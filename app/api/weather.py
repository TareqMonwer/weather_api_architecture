import logging
from fastapi import APIRouter

from app.services.cache_services.redis_cache_service import RedisCacheService
from app.services.weather_service import WeatherService

logger = logging.getLogger("weather_api")

router = APIRouter()


@router.get("/")
async def get_weather(city: str):
    is_cached = await RedisCacheService().cache_exists(city)
    if is_cached:
        return await RedisCacheService().get(city)

    weather = await WeatherService("http").get(city)
    if weather and weather.get("list"):
        await RedisCacheService().set(city, weather)

    return weather
