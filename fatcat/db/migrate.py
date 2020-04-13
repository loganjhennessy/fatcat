import os
import sqlite3

import click


def get_migration_paths():
    migration_filenames = os.listdir("migrations")
    return [f"migrations/{filename}" for filename in migration_filenames]


def get_migration_sql(migration_path):
    with open(migration_path, "r") as f:
        return f.read()


@click.command()
@click.option('--dbpath', default='db/fatcat.db')
def run_db_migrations(dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    migrations = get_migration_paths()

    try:
        for migration in migrations:
            sql = get_migration_sql(migration)
            cur.executescript(sql)
    except sqlite3.Error as e:
        print(e)
    conn.commit()
    conn.close()
