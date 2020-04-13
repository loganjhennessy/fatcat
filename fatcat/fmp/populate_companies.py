import sqlite3
from typing import Dict, List

import click

from fatcat.fmp.request_helpers import make_prepped_url
from fatcat.fmp.request_helpers import make_request


def insert_company(company_profile):
    con = sqlite3.connect('db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    with con:
        cur.execute('INSERT INTO company(symbol, name, description, industry, sector, exchange, website, ceo) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (company_profile['symbol'],
                     company_profile['companyName'],
                     company_profile['description'],
                     company_profile['industry'],
                     company_profile['sector'],
                     company_profile['exchange'],
                     company_profile['website'],
                     company_profile['ceo']))


def get_company_profile(symbol) -> Dict:
    company_profile_url = f'https://fmpcloud.io/api/v3/profile/{symbol}'
    prepped_url = make_prepped_url(company_profile_url)
    response = make_request(prepped_url)
    return response.json()


def get_symbol_list() -> List[Dict]:
    symbol_list_url = 'https://fmpcloud.io/api/v3/stock/list'
    prepped_url = make_prepped_url(symbol_list_url)
    response = make_request(prepped_url)
    print(response)
    symbols_list = [symbol['symbol'] for symbol in response.json()]
    return symbols_list


@click.command()
def populate_companies():
    symbol_list = get_symbol_list()
    for symbol in symbol_list[:2]:
        company_profile = get_company_profile(symbol)
        print(company_profile[0])
        insert_company(company_profile[0])
