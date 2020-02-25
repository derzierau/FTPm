from freilanz.logging import logger
from freilanz.database import Database
from freilanz.config import Config
from freilanz.helper import get_profile_and_projects_from_path, ACTION_TYPES
log = logger(__name__)


def status(click, **kwargs):
    config = Config()
    path_profile = get_profile_and_projects_from_path(config.root_dir())
    db = Database()
    _sum = db.get_sum_by_profile_project(
        path_profile['profile'], path_profile['current_project'])
    open_timer = db.open_timer()
    text = f"Status: \nDurations: \n"
    
    text += f"{_sum}\n"
    if not open_timer.empty:
      text += f'Open Timer: \n{open_timer}'
    else:
      text += f'No open timer.'
    click.echo(text)
