# coding=utf-8
import logging
from warnings import filterwarnings

import paramiko
from cryptography.utils import CryptographyDeprecationWarning

# 忽略特定警告
filterwarnings("ignore", category=CryptographyDeprecationWarning)

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_ssh_connection(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        logging.info(f"Connected to {hostname}")
    except Exception as e:
        logging.error(f"Failed to connect to {hostname}: {e}")
        raise
    return ssh


def run_command(ssh, command):
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout_output = stdout.read().decode()
        stderr_output = stderr.read().decode()
        if stdout_output:
            logging.info(f"Command output: {stdout_output}")
        if stderr_output:
            logging.error(f"Command error: {stderr_output}")
    except Exception as e:
        logging.error(f"An error occurred while running command: {e}")


def transfer_files(ssh, local_path, remote_path, direction='upload'):
    sftp = None
    try:
        sftp = ssh.open_sftp()
        if direction == 'upload':
            sftp.put(local_path, remote_path)
            logging.info(f"Uploaded {local_path} to {remote_path}")
        elif direction == 'download':
            sftp.get(remote_path, local_path)
            logging.info(f"Downloaded {remote_path} to {local_path}")
    except Exception as e:
        logging.error(f"An error occurred while transferring files: {e}")
    finally:
        if sftp:
            sftp.close()


if __name__ == '__main__':
    hostname = '123.57.135.65'
    port = 22
    username = 'root'
    password = 'root'

    ssh = None
    try:
        ssh = setup_ssh_connection(hostname, port, username, password)

        run_command(ssh, 'ls -l')

        # 上传文件
        # transfer_files(ssh, 'local_file.txt', 'remote_path.txt', direction='upload')

        # 下载文件
        transfer_files(ssh, 'local_file_from_server.txt', 'remote_path.txt', direction='download')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if ssh:
            try:
                ssh.close()
                logging.info("SSH connection closed")
            except Exception as e:
                logging.error(f"An error occurred while closing SSH connection: {e}")
