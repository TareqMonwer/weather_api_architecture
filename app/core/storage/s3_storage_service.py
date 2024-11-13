import logging
import boto3
from botocore.exceptions import NoCredentialsError
from app.core.storage.storage_service_abc import StorageServiceAbc
from app.config.settings import settings

logger = logging.getLogger("weather_api")


class S3StorageService(StorageServiceAbc):
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
        )

    def upload_file(self, file_name: str, file_data: bytes):
        try:
            self.s3_client.put_object(
                Bucket=settings.AWS_BUCKET_NAME, Key=file_name, Body=file_data
            )
            logger.info(
                f"New file uploaded at: s3://{settings.AWS_BUCKET_NAME}/{file_name}"
            )
        except NoCredentialsError:
            raise ValueError("AWS credentials are not configured properly")
