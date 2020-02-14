import os
from helper import split, ROOT_PROJECT_PATH
from config import get_config
import logging

log = logging.getLogger(__name__)


class Project():
    def __init__(self):
        self.current_path = os.getcwd()
        self.current_project = split(self.current_path)[-1]
        self.current_account = split(split(self.current_path)[-2])[-1]
        self.config = get_config()

    def init(self):
        for account in self.config['accounts']:
            for project in account['projects']:
                Project.generate_new_project(
                    account['short_name'], project['short_name'])

    @staticmethod
    def generate_new_project(account: str, project_name: str):
        try:
            path = f'{ROOT_PROJECT_PATH}/{account}/{project_name}'
            log.info(f'Adding Project to {path}')
            os.makedirs(path)
        except FileExistsError as e:
            log.error(f'File {path} exists')

    @staticmethod
    def generate_new_account(account: str):
        try:
            os.makedirs(f'{account}')
        except OSError as e:
            raise e
