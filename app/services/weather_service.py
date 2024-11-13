import datetime
import json
from app.services.cache_services.redis_cache_service import RedisCacheService
from app.services.external_api.http_weather_fetcher import HttpWeatherFetcher
from app.services.weather_fetcher_abc import WeatherFetcherAbc
from app.services.weather_report_service.weather_report_service import (
    WeatherReportService,
)


class WeatherService:
    def __init__(self, strategy_key: str) -> None:
        self.__fetcher: WeatherFetcherAbc = self.__get_fetcher(strategy_key)

    def set_http_fetcher(self) -> HttpWeatherFetcher:
        url = "https://api.openweathermap.org/data/2.5/find?q={}&appid=5796abbde9106b7da4febfae8c44c232&units=metric"
        return HttpWeatherFetcher(api_url=url)

    def __get_fetcher(self, strategy_key: str) -> HttpWeatherFetcher:
        match strategy_key:
            case "http":
                return self.set_http_fetcher()
            case _:
                return self.set_http_fetcher()

    async def get_weather(self, city: str):
        return await self.__fetcher.get(city)

    async def get(self, city: str):
        is_cached = await RedisCacheService().cache_exists(city)

        if is_cached:
            return await RedisCacheService().get(city)

        fetcher: HttpWeatherFetcher = self.__get_fetcher("http")
        weather = await fetcher.get(city)

        if weather and weather.get("list"):
            await RedisCacheService().set(city, weather)

            # TODO: perform s3 upload and event publish task here.
            file_name = str(datetime.datetime.now().date()) + city
            json_bytes = json.dumps(weather).encode("utf-8")
            WeatherReportService().store_weather_data(file_name, json_bytes)
        return weather
