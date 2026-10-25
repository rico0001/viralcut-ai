from typing import Any, Dict

class StorageService:
    def __init__(self, storage_provider: Any):
        self.storage_provider = storage_provider

    def upload_file(self, file_path: str, user_id: str) -> str:
        return self.storage_provider.upload(file_path, user_id)

    def download_file(self, file_id: str) -> str:
        return self.storage_provider.download(file_id)

    def delete_file(self, file_id: str) -> None:
        self.storage_provider.delete(file_id)

    def list_files(self, user_id: str) -> Dict[str, Any]:
        return self.storage_provider.list(user_id)

    def get_file_metadata(self, file_id: str) -> Dict[str, Any]:
        return self.storage_provider.get_metadata(file_id)