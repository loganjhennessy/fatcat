import functools
import pickle
import sqlite3
from typing import Dict, List

import click
import requests

from fatcat.fmp.request_helpers import make_prepped_url
from fatcat.fmp.request_helpers import make_request

sqlite3.register_converter("pickle", pickle.loads)
sqlite3.register_adapter(requests.Response, pickle.dumps)


# def check_cache(check_cached_func, cache_response_func):
#     def decorator_check_cache(func):
#         @functools.wraps(func)
#         def get_wrapper(*args):
#             url = args[0]
#             cache_results = check_cached_func(url)
#             if not cache_results:
#                 response = func(url)
#                 cache_response_func(url, response)
#                 return response
#             else:
#                 return cache_results
#         return get_wrapper
#     return decorator_check_cache
#
#
# def check_cache_func(url):
#     con = sqlite3.connect('../db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     with con:
#         cur.execute("SELECT * FROM request_cache where url = ?", (url,))
#
#     response = cur.fetchone()
#     if not response:
#         con.close()
#     else:
#         response = response['response']
#         con.close()
#     return response
#
#
# def cache_response_func(url, response):
#     con = sqlite3.connect('../db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     with con:
#         cur.execute("INSERT INTO request_cache VALUES (?, ?)", (url, response))
#
#     con.close()
#
#
# def make_prepped_url(url: str, params: Dict[str, str]={}) -> str:
#     params['apikey'] = config.api_key
#     request = requests.Request(
#         url=url,
#         params=params
#     )
#     return request.prepare().url
#
#
# @check_cache(check_cache_func, cache_response_func)
# def make_request(url: str) -> requests.Response:
#     return requests.get(url)


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
    symbols_list = [symbol['symbol'] for symbol in response.json()]
    return symbols_list


@click.command()
def populate_companies():
    symbol_list = get_symbol_list()
    for symbol in symbol_list[:2]:
        company_profile = get_company_profile(symbol)
        print(company_profile[0])
        insert_company(company_profile[0])
