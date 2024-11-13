import abc


class StorageServiceAbc(abc.ABC):
    @abc.abstractmethod
    def upload_file(self, file_name: str, file_data: bytes) -> None:
        pass
