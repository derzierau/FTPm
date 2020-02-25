from freilanz.logging import logger
from freilanz.helper import FREILANZ_ROOT_DIR, make_dir, CONFIG_FILE_NAME
from freilanz.config import init_base_config
log = logger(__name__)


def init(click, *args, **kwargs):
    log.info('start init process')
    click.echo('Starting initializing process')
    root_dir = FREILANZ_ROOT_DIR

    

    if root_dir:
        root_dir_question = click.confirm(
            f'Should we use {FREILANZ_ROOT_DIR} as the root dir?')
        if not root_dir_question:
            root_dir = click.prompt('Where do you want to set the root dir?')

        click.echo(f'Set up root dir {root_dir}')
        make_dir(root_dir, exist_ok=True)


    init_base_config(**kwargs, root_dir=root_dir)
    if init_base_config:
      click.echo(f'Added base config file to {root_dir}/{CONFIG_FILE_NAME}')
      open_it = click.confirm('Would you like to open the config file?')
      if open_it:
        click.edit(filename=f'{root_dir}/{CONFIG_FILE_NAME}')