import os
from typing import List

import paramiko
from ..domain.image import Image
from ..domain.repository import AbstractDownloadRepository


class ImageDownloadRepository(AbstractDownloadRepository):
    def __init__(self, ssh_password:str, ssh_host:str, ssh_user:str):
        self.ssh_password = ssh_password
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user

    def download_remote_content(self, images:List[Image], local_path:str, remote_path:str):
        local_paths = []
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ssh_host, username=self.ssh_user, password=self.ssh_password)
        sftp = ssh.open_sftp()
        for image in images:
            actual_remote_path = os.path.join(remote_path, image.stone_type, str(image.id) + ".jpg")
            actual_local_path = os.path.join(local_path, str(image.id) + ".jpg")
            print('downloading ' + actual_remote_path + ' into ' + actual_local_path)
            sftp.get(actual_remote_path, actual_local_path)
            local_paths.append(actual_local_path)

        sftp.close()
        ssh.close()
        return local_paths
