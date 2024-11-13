from app.core.storage.storage_service_abc import StorageServiceAbc


class StorageService(StorageServiceAbc):
    def upload_file(self, file_name: str, file_data: bytes) -> None:
        raise NotImplementedError("Must implement 'upload_file' method")
