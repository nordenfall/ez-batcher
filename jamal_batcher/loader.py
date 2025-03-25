import os
from typing import Literal
from .application.batcher import BatchProcessor
from .infrastructure.images_downloader import ImageDownloadRepository
from .infrastructure.repository_sql import SQLOperationRepository
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")
ssh_host = os.getenv("SSH_HOST")
ssh_user = os.getenv("SSH_USER")
remote_path = os.getenv("REMOTE_PATH")
ssh_password = os.getenv("SSH_PASSWORD")


class Connect:
    def __init__(self):
        self.db_url = db_url
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.remote_path = remote_path
        self.ssh_password = ssh_password

class BatchGenerator:
    def __init__(self, con:Connect, local_path, batch_size, stone_type:Literal["acid", "carbonatap", "struvit", "wedelit", "wewelit"]):
        self.con = con
        self.local_path = local_path
        self.batch_size = batch_size
        self.stone_type = stone_type
        self.sql_repo = SQLOperationRepository(db_url=con.db_url)
        self.download_repo = ImageDownloadRepository(ssh_password=con.ssh_password, ssh_host=con.ssh_host, ssh_user=con.ssh_user)
        self.processor = BatchProcessor(self.sql_repo, self.download_repo)

    def generate_batch(self):
        processor = BatchProcessor(self.sql_repo, self.download_repo)  
        images = processor.get_batch(self.batch_size, self.stone_type, self.local_path, self.con.remote_path)
        self.sql_repo.close_connection()
        return images
    
__all__=["BatchGenerator"]

        



