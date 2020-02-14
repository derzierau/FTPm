import yaml
import pickle
from helper import CONFIG_PATH

def import_config(path: str):
  if not path: raise AttributeError
  with open(path) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    pickle.dump(config, open(CONFIG_PATH, 'wb'))

def get_config():
  try:
    return pickle.load(open(CONFIG_PATH, 'r'))
  except:
    return None
  