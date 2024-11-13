from typing import Any

import httpx
from app.services.weather_fetcher_abc import WeatherFetcherAbc


class HttpWeatherFetcher(WeatherFetcherAbc):
    def __init__(self, api_url: str) -> None:
        """api_placeholder must provide a format string for city to be applied .format() on.
        ie. 'example.com/weather?token=alreadyAvailableToken&city={}' here {} is for placeholder.
        """
        self.api_placeholder = api_url

    async def get(self, city: str) -> Any:
        url = self.api_placeholder.format(city)

        async with httpx.AsyncClient() as client:
            resp = await client.get(url)

        return resp.json()
