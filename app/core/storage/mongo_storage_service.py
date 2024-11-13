from app.core.storage.storage_service_abc import StorageServiceAbc


class MongoStorageService(StorageServiceAbc):
    def upload_file(self, file_name: str, file_data: bytes):
        print("MongoStorageService upload_file not implemented.")
