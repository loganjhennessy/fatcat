import json

import requests

BASE_URL = "https://www.googleapis.com/sql/v1beta4/projects/"
CLOUDSQL_INSTANCE_ENDPOINT = "{project_id}/instances"
CLOUDSQL_DATABASE_ENDPOINT = "{project_id}/instances/{instance}/databases"


def create_database_instance():
    with open("sql/database-instance.json", "r") as f:
        database_instance = json.loads(f.read())
        requests.post(BASE_URL + CLOUDSQL_INSTANCE_ENDPOINT.format(project_id="fatcat-app"), data=database_instance)


def create_database():
    with open("sql/database-instance.json", "r") as f:
        database = json.loads(f.read())
        requests.post(BASE_URL + CLOUDSQL_DATABASE_ENDPOINT.format(project_id="fatcat-db"), data=database)


def main():
    create_database_instance()
    create_database()


if __name__ == "__main__":
    main()
