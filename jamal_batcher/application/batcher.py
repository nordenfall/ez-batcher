from ..domain.repository import AbstractDownloadRepository, AbstractImageRepository


class BatchProcessor:
    def __init__(self, repo:AbstractImageRepository, downloader:AbstractDownloadRepository):
        self.repo = repo
        self.downloader = downloader
        
    def get_batch(self, batch_size:str, stone_type:str, local_path:str, remote_path:str):
        images = self.repo.get_unused_images(batch_size=batch_size, stone_type=stone_type)
        if not images:
            return
        
        download_and_get_list = self.downloader.download_remote_content(images=images, local_path=local_path, remote_path=remote_path)
        self.repo.mark_as_used(images=images)

        return download_and_get_list