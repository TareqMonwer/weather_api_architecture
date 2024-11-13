from datetime import timedelta
import json
import logging
from typing import Any

from redis.asyncio.client import Redis
from app.services.cache_services.cache_service_abc import CacheServiceAbc
from app.db.redis_client import client as redis_client

logger = logging.getLogger("weather_api")


class RedisCacheService(CacheServiceAbc):
    __client: Redis = redis_client

    async def get(self, key: str) -> str | None:
        byte_data: bytes | None = await RedisCacheService.__client.get(key)

        if byte_data:
            try:
                str_data = byte_data.decode("utf-8").replace("'", '"')
                dict_data = json.loads(str_data)
                return dict_data
            except Exception as e:
                logger.error(e)
        return None

    async def cache_exists(self, key: str) -> bool:
        ttl = await RedisCacheService.__client.ttl(key)
        return ttl > 0

    async def set(self, key: str, value: Any) -> None:
        try:
            await redis_client.set(key, str(value).encode())
            await RedisCacheService.__client.setex(
                key, timedelta(minutes=5), value
            )
        except Exception as e:
            logger.error(e)
