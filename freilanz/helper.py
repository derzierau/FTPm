import os
from appdirs import AppDirs

CONFIG_FILE_NAME = '.lanzconfig.yaml'

ACTION_TYPES = {
    'start': 'start',
    'end': 'end',
    'task': 'task'
}

DIRS = AppDirs('freilanz', 'Ole Zierau')

current_dir = os.getcwd()
config_dir = DIRS.user_config_dir
data_dir = DIRS.user_data_dir
log_dir = DIRS.user_log_dir
home_dir = os.environ.get('HOME')
FREILANZ_ROOT_DIR = os.environ.get(
    'FREILANZ_ROOT_DIR') if 'FREILANZ_ROOT_DIR' in os.environ else f'{home_dir}/projects'

os.makedirs(config_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

os.makedirs(log_dir, exist_ok=True)
os.makedirs(home_dir, exist_ok=True)



def get_profile_and_projects_from_path(root_dir: str, path: str = os.getcwd()):
  p = path.split(root_dir)[1]
  projects = p.split('/')[2:]
  current_project = None
  if len(projects) > 0:
    current_project = projects[-1]

  return {
    'profile': p.split('/')[1],
    'projects': projects,
    'current_project': current_project
  }


def make_dirs(projects: list, root_dir: str, **kwargs):
    if len(projects) > 0:
        for project in projects:
            path = f"{root_dir}/{project['id']}"
            print(f'Created {path}')
            os.makedirs(path, exist_ok=True)
            if 'projects' in project:
                make_dirs(project['projects'], path)


def make_dir(path: str, **kwargs):
    return os.makedirs(path, **kwargs)


def split(path: str):
    return os.path.split(path)
