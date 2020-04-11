import click

from api.db.migrate import run_db_migrations
from api.jobs import populate_companies

@click.group()
def cli():
    pass


cli.add_command(run_db_migrations)