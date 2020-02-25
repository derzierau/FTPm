from freilanz.database import Database
from freilanz.logging import logger
from freilanz.helper import ACTION_TYPES, get_profile_and_projects_from_path
from freilanz.config import Config
from freilanz.database import Database
from datetime import datetime
from os import getcwd

log = logger(__name__)
def stop(click, **kwargs):
  config = Config()
  path_profile = get_profile_and_projects_from_path(config.root_dir())
  
  entry = {
    'timestamp': datetime.now(),
    'profile': kwargs.get('profile', path_profile['profile']) or path_profile['profile'],
    'project': kwargs.get('project', path_profile['current_project']) or path_profile['current_project'],
    'path': getcwd(),
    'message': kwargs.get('message'),
    'service': kwargs.get('service') or config.default_service()['id'],
    'action': ACTION_TYPES['end']
  }
  Database().insert(entry)
  click.echo(f"Stopped timer for {path_profile['profile']}/{'/'.join(path_profile['projects'])}")
  log.debug('starting timer call')
  