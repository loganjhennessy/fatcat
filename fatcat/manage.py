import click

from fatcat.db.migrate import run_db_migrations
from fatcat.fmp.populate_companies import populate_companies


@click.group()
def cli():
    pass


cli.add_command(run_db_migrations)
cli.add_command(populate_companies)

if __name__ == '__main__':
    cli()
