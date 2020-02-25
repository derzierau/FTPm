import yaml
import json
import logging
import glob
import os
import pathlib
from freilanz.helper import config_dir, DIRS, CONFIG_FILE_NAME, current_dir, FREILANZ_ROOT_DIR

log = logging.getLogger(__name__)


def find_config_file(current_dir: str = current_dir) -> str or None:
    root = pathlib.Path(current_dir).root
    files = list(pathlib.Path(current_dir).glob(CONFIG_FILE_NAME))
    parent = pathlib.Path(current_dir).parent
    if len(files) == 1:
        return files[0]

    elif str(parent) != str(root):
        return find_config_file(parent)
    else:
        return None


def import_config(path: str = find_config_file):
    if not path:
        raise AttributeError
    with open(path) as file:
        config = yaml.load(file)
        with open(config_dir + '/config.json', 'w') as json_file:
            json.dump(config, json_file)


def init_base_config(**kwargs):
    config = {
        'profiles': [],
        'base': {
            'user': {
                'name': kwargs.get('name'),
                'address': {
                    'city': kwargs.get('city'),
                    'zip_code': kwargs.get('zip_code'),
                    'street': kwargs.get('street'),
                    'country': kwargs.get('country'),
                },
                'invoices': {
                    'iban': kwargs.get('iban'),
                    'currency': kwargs.get('currency'),
                },
                'environment': {
                    'root_dir': kwargs.get('root_dir')
                }
            }
        },
        'positions': [
            {
                'name': 'Developer',
                'hourly_rate': 65,
                'id': 'dev',
                'default': True
            }
        ]
    }

    with open(kwargs.get('root_dir') + '/' + CONFIG_FILE_NAME, 'w') as file:
        yaml.dump(config, file)

    return config


def get_config():
    config_file = find_config_file(os.getcwd())
    if config_file:
        try:
            return yaml.load(open(config_file, 'rb'), Loader=yaml.SafeLoader)
        except OSError as error:
            log.error('Not able to load config', error)

    return None


class Config:
    def __init__(self):
        self.config = get_config()
    
    def root_dir(self):
        return self.config['base']['user']['environment']['root_dir']

    def get_project_config(self, account_name, project_name):
        accounts = self.config['profiles'] if 'profiles' in self.config and len(
            self.config['profiles']) > 0 else None
        if accounts:
            account = [
                account for account in accounts if 'id' in account and account['id'] == account_name]
            if (len(account) > 0):
                project = [
                    project for project in account[0]['projects'] if project['id'] == project_name]
                if (len(project) > 0):
                    return project[0]
                else:
                    raise BaseException('Project not found')
            else:
                raise 'Profile not found'
        else:
            raise 'Profiles not available'

    def default_service(self):
        services = self.get_positions()
        if services:
            default = [
                service for service in services if 'default' in service and service['default'] == True]
            return default[0]
        return self.get_positions()[0]

    def get_positions(self, short_name=None):
        if not self.config:
            raise FileNotFoundError
        if short_name:
            return [service for service in self.config['positions'] if service['id'] == short_name][0]
        return self.config['positions']
