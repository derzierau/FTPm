from freilanz.database import Database
from freilanz.logging import logger
from freilanz.helper import ACTION_TYPES, get_profile_and_projects_from_path
from freilanz.config import Config
from freilanz.database import Database
from datetime import datetime
import pandas as pd
from os import getcwd

log = logger(__name__)


def start(click, **kwargs):
    config = Config()
    path_profile = get_profile_and_projects_from_path(config.root_dir())
    project = path_profile['current_project']
    if kwargs.get('ago'):
      time = pd.Timestamp('now') - pd.Timedelta(kwargs.get('ago'))
    else:
      time = datetime.now()
    entry = {
        'timestamp': time,
        'profile': kwargs.get('profile', path_profile['profile']) or path_profile['profile'],
        'project': kwargs.get('project', project) or project,
        'path': getcwd(),
        'message': kwargs.get('message'),
        'service': kwargs.get('service') or config.default_service()['id'],
        'action': ACTION_TYPES['start']
    }
    Database().insert(entry)
    click.echo(
        f"Started timer for {path_profile['profile']}/{'/'.join(path_profile['projects'])} on {time}")
    log.debug('starting timer call')
    pass
