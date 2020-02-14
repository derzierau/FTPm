import yaml
import pickle
from helper import CONFIG_PATH

def import_config(path: str):
  if not path: raise AttributeError
  with open(path) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    print(config)
    pickle.dump(config, open(CONFIG_PATH, 'wb'))

def get_config():
  try:
    return pickle.load(open(CONFIG_PATH, 'rb'))
  except OSError as error:
    print(error)
  