import click
from project_manager import Project
from config import import_config
from timer import Timer
from stats import Stats
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@click.group()
def cli():
    pass


@click.command('init')
@click.argument('CONFIG_FILE_PATH', required=True)
def init(config_file_path):

    import_config(config_file_path)

    Project().init()


@click.command('start')
@click.option('-m', '--message', default=None, help="Message to save with starting job")
@click.option('-s', '--service', default=None, help="Your service short_name, defaults to the first entry of config services")
@click.option('-a', '--account', default=None, help="Your service short_name, defaults to the first entry of config services")
@click.option('-p', '--project', default=None, help="Your service short_name, defaults to the first entry of config services")
def start_timer(message, service, account, project):
    entry = Timer().start_time(message=message, service=service, account=account, project=project)
    click.echo(f"Starting timer for {entry['account']}/{entry['project']}")


@click.command('end')
@click.option('--project', default=None, help="Specify a project")
def end_timer(project: str):
    ended_timers = Timer().end_timer()
    if ended_timers:
        for entry in ended_timers:
            if entry and 'path' in entry:
                click.echo(f"Ended timer for {entry['path']}")
    else:
        click.echo('No timer started')


@click.command('stats')
def stats():
    click.echo(Stats().duration_sum_by_key('path'))

cli.add_command(start_timer)
cli.add_command(end_timer)
cli.add_command(init)
cli.add_command(stats)


if __name__ == "__main__":
    cli()
