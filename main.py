import os
import sys
from logging import FileHandler

from synchronizer import Synchronizer
from logger import logger, formatter


def check_path_exists(path):
    return os.path.exists(path)


def check_time(_time):
    return _time.isdigit()


args = sys.argv[1:]
source_folder_path = args[0]
replica_folder_path = args[1]
sync_time = args[2]
log_path = args[3]

if log_path:
    file_log = FileHandler(log_path)
else:
    file_log = FileHandler('log.txt')
file_log.setFormatter(formatter)
logger.addHandler(file_log)

if check_path_exists(source_folder_path) and check_path_exists(replica_folder_path) and check_time(sync_time):
    sync_task = Synchronizer(source_folder_path, replica_folder_path, sync_time)
    sync_task.synchronize_folders()
else:
    logger.error('Wrong data')
