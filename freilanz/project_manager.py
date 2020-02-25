import os
from freilanz.helper import split, FREILANZ_ROOT_DIR
from freilanz.config import get_config
import logging

log = logging.getLogger(__name__)


class Project():
    def __init__(self):
        self.current_path = os.getcwd()
        self.current_project = split(self.current_path)[-1]
        self.current_account = split(split(self.current_path)[-2])[-1]
        self.config = get_config()

    def init(self):
        for profile in self.config['profiles']:
            for project in profile['projects']:
                Project.generate_new_project(
                    profile['id'], project)

    @staticmethod
    def generate_new_project(account: str, project):
        try:
            path = f"{FREILANZ_ROOT_DIR}/{account}/{project['id']}"
            log.info(f'Adding Project to {path}')
            os.makedirs(path)
            if 'repo' in project and project['repo']:
                try:
                    os.system(f"git clone {project['repo']} {path}")
                except OSError as error:
                    log.error(error)
                else:
                    pass
        except FileExistsError as e:
            log.error(f'File {path} exists')

    @staticmethod
    def generate_new_account(account: str):
        try:
            os.makedirs(f'{account}')
        except OSError as e:
            raise e
