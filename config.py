import yaml
import pickle
def import_config(path: str):
  if not path: raise AttributeError
  with open(path) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    pickle.dump(config, open('config.pickle', 'wb'))

def get_config():
  return pickle.load(r'config.pickle')