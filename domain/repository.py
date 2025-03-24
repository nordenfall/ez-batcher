from abc import ABC
from typing import List
from domain.image import Image

class AbstractImageRepository(ABC):
    @classmethod
    def get_unused_images(self, batch_size:int, stone_type:str) -> List[Image]: ...

    @classmethod
    def mark_as_used(self, images:List[Image]): ...

    @classmethod
    def close_connection(self): ...

class AbstractDownloadRepository(ABC):
    @classmethod
    def download_remote_content(self, images:List[Image], local_path:str, remote_path:str): ...