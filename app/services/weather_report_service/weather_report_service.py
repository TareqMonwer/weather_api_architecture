from app.config.settings import settings
from app.core.storage.mongo_storage_service import MongoStorageService
from app.core.storage.s3_storage_service import S3StorageService


class WeatherReportService:
    def __init__(self):
        if settings.AWS_ACCESS_KEY and settings.AWS_SECRET_KEY:
            self.storage_service = S3StorageService()
        else:
            self.storage_service = MongoStorageService()

    def store_weather_data(self, file_name: str, file_data: bytes):
        return self.storage_service.upload_file(file_name, file_data)
