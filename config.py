import yaml
import json
from helper import CONFIG_PATH
import logging

log = logging.getLogger(__name__)

def import_config(path: str):
  if not path: raise AttributeError
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

  def default_service(self):
    services = self.get_services()
    if services:
      default = [service for service in services if 'default' in service and service['default'] == True]
      return default[0]
    return self.get_services()[0]

  def get_services(self):
    if not self.config: raise FileNotFoundError
    return self.config['services']