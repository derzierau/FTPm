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
    db = Database()
    path_profile = get_profile_and_projects_from_path(config.root_dir())
    project = path_profile['current_project']
    # Check if timers are still open in same profile
    open_timer = db.open_timer()
    if not open_timer.empty:
        sure = click.confirm(
            f'{open_timer.to_string()}\n These timers are still open. Would you like to stop them?', abort=True)
        if sure:
            # Stop timer
            for index, entry in open_timer.iterrows():
                del entry['id']
                _entry = {
                    **entry,
                    'timestamp': datetime.now(),
                    'action': ACTION_TYPES['end']
                }
                db.insert(_entry)
            
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
    db.insert(entry)
    click.echo(
        f"Started timer for {path_profile['profile']}/{'/'.join(path_profile['projects'])} on {time}")
    log.debug('starting timer call')
    pass
