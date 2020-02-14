import os
import sys
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
DB_PATH = f'{ROOT_DIR}/db.csv'

def split(path: str):
  return os.path.split(path)

