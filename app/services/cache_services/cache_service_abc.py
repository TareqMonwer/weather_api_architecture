import abc
from typing import Any


class CacheServiceAbc(abc.ABC):
    @abc.abstractmethod
    async def get(self, key: str) -> str | None:
        pass

    @abc.abstractmethod
    async def cache_exists(self, key: str) -> bool:
        pass

    @abc.abstractmethod
    async def set(self, key: str, value: Any) -> None:
        pass
