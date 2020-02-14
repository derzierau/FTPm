import click
from project_manager import Project
from config import import_config
from timer import start_time
project = Project()


@click.group()
def cli():
  pass

@click.command('init')
@click.argument('CONFIG_FILE_PATH', required=True)
def init(config_file_path):
  import_config(config_file_path)

@click.command('start')
def start_timer():
  entry = start_time()
  click.echo(f"Starting timer for {entry['account']}/{entry['project']}")


@click.command('end')
@click.option('--project', default=None, help="Specify a project")
def end_timer(project: str):
  click.echo(project)

cli.add_command(start_timer)
cli.add_command(end_timer)
cli.add_command(init)

if __name__ == "__main__":
    cli()