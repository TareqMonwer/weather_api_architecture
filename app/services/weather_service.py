from app.services.http_weather_fetcher import HttpWeatherFetcher
from app.services.weather_fetcher_abc import WeatherFetcherAbc


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

    async def get(self, city: str):
        if not self.__fetcher:
            raise ValueError(
                "WeatherService.set_<type>_fetcher() must be called \
                before using WeatherService.get()"
            )
        return await self.__fetcher.get(city)
