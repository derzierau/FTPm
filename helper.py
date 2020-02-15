import os
import sys
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
DB_PATH = f'{ROOT_DIR}/db.csv'
DB_PATH_HD5 = f'{ROOT_DIR}/db.h5'
CONFIG_PATH = f'{ROOT_DIR}/config.json'

ROOT_PROJECT_PATH = f"{os.getenv('HOME')}/projects"



START_TIMER_ACTION = 'start_timer_action'
END_TIMER_ACTION = 'end_timer_action'




def split(path: str):
  return os.path.split(path)

