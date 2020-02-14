import click
from project_manager import Project
from config import import_config
from timer import Timer
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@click.group()
def cli():
    pass


@click.command('init')
@click.argument('CONFIG_FILE_PATH', required=True)
def init(config_file_path):

    import_config(config_file_path)

    Project().init()


@click.command('start')
def start_timer():
    entry = Timer().start_time()
    click.echo(f"Starting timer for {entry['account']}/{entry['project']}")


@click.command('end')
@click.option('--project', default=None, help="Specify a project")
def end_timer(project: str):
    Timer().end_timer()


cli.add_command(start_timer)
cli.add_command(end_timer)
cli.add_command(init)

if __name__ == "__main__":
    
    cli()
