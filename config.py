import yaml
import json
from helper import CONFIG_PATH
import logging

log = logging.getLogger(__name__)


def import_config(path: str):
    if not path:
        raise AttributeError
    with open(path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        with open(CONFIG_PATH, 'w') as json_file:
            json.dump(config, json_file)


def get_config():
    try:
        return json.load(open(CONFIG_PATH, 'rb'))
    except OSError as error:
        log.error('Not able to load config', error)


class Config:
    def __init__(self):
        self.config = get_config()

    def get_project_config(self, account_name, project_name):
        accounts = self.config['accounts'] if 'accounts' in self.config and len(
            self.config['accounts']) > 0 else None
        if accounts:
            account = [
                account for account in accounts if 'short_name' in account and account['short_name'] == account_name]
            if (len(account) > 0):
                project = [
                    project for project in account[0]['projects'] if project['short_name'] == project_name]
                if (len(project) > 0):
                  return project[0]
                else:
                  raise BaseException('Project not found')
            else:
              raise 'Account not found'
        else: 
          raise 'Accounts not available'     
    def default_service(self):
        services = self.get_services()
        if services:
            default = [
                service for service in services if 'default' in service and service['default'] == True]
            return default[0]
        return self.get_services()[0]

    def get_services(self, short_name = None):
        if not self.config:
            raise FileNotFoundError
        if short_name:
          return [service for service in self.config['services'] if service['short_name'] == short_name][0]
        return self.config['services']
