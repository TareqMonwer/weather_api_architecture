import abc
from typing import Any


class WeatherFetcherAbc(abc.ABC):
    @abc.abstractmethod
    def get(self, city: str) -> Any:
        pass
