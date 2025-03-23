import os
from typing import Literal
import paramiko
import psycopg2

db_url = os.getenv("DB_URL")
ssh_host = os.getenv("SSH_HOST")
ssh_user = os.getenv("SSH_USER")
remote_path = os.getenv("REMOTE_PATH")
ssh_password = os.getenv("SSH_PASSWORD")

class BatchGenerator:
    def __init__(self, local_path, batch_size, stone_type:Literal["acid", "carbonatap", "struvit", "wedelit", "wewelit"]):
        self.local_path = local_path
        self.ssh_password = ssh_password
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.remote_path = remote_path
        self.batch_size = batch_size
        self.stone_type = stone_type

        self.db = psycopg2.connect(db_url)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=self.ssh_host, username=self.ssh_user, password=self.ssh_password)

        sftp = ssh.open_sftp()
        



