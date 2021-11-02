import os
import shutil
import time

from logger import logger


def define_action_with_path(_path, _command):
    tested_path = os.path.splitext(_path)
    if tested_path[-1]:
        return _command + '_file'
    else:
        return _command + '_directory'


def action_with_path(_action):
    action_dict = {'copy_file': shutil.copyfile,
                   'delete_file': os.remove,
                   'copy_directory': shutil.copytree,
                   'delete_directory': shutil.rmtree}
    return action_dict.get(_action)


def edit_replica(folder_1, folder_2, action):
    for element in os.listdir(folder_1):
        if element not in os.listdir(folder_2):
            path = os.path.join(folder_1, element)
            raw_cmd = define_action_with_path(path, action)
            cmd = action_with_path(raw_cmd)
            if action == 'copy':
                destination_path = os.path.join(folder_2, element)
                cmd(path, destination_path)
                logger.info(f'{element} copied in replica folder')
            else:
                cmd(path)
                logger.info(f'{element} deleted from replica folder')


class Synchronizer:
    def __init__(self, source_folder, replica_folder, sync_time):

        self.sync_time = float(sync_time)
        self.source_folder = source_folder
        self.replica_folder = replica_folder
        self.enable = True

    def synchronize_folders(self):
        while self.enable:
            edit_replica(self.source_folder, self.replica_folder, 'copy')
            edit_replica(self.replica_folder, self.source_folder, 'delete')

            try:
                time.sleep(self.sync_time)
            except KeyboardInterrupt:
                self.enable = False
