import functools
import pickle
import sqlite3
from typing import Dict

import requests

from fatcat.config import config
from fatcat.db import db_connect

sqlite3.register_converter("pickle", pickle.loads)
sqlite3.register_adapter(requests.Response, pickle.dumps)


def check_cache(check_cached_func, cache_response_func):
    def decorator_check_cache(func):
        @functools.wraps(func)
        def get_wrapper(*args):
            url = args[0]
            cache_results = check_cached_func(url)
            if not cache_results:
                response = func(url)
                cache_response_func(url, response)
                return response
            else:
                return cache_results
        return get_wrapper
    return decorator_check_cache


def check_cache_func(url):
    # con = sqlite3.connect('db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con = db_connect()
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM request_cache where url = ?", (url,))

    response = cur.fetchone()
    if not response:
        con.close()
    else:
        response = response['response']
        con.close()
    return response


def cache_response_func(url, response):
    # con = sqlite3.connect('db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con = db_connect()
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    with con:
        cur.execute("INSERT INTO request_cache VALUES (?, ?)", (url, response))

    con.close()


def make_prepped_url(url: str, params: Dict[str, str]={}) -> str:
    params['apikey'] = config.api_key
    request = requests.Request(
        url=url,
        params=params
    )
    return request.prepare().url


@check_cache(check_cache_func, cache_response_func)
def make_request(url: str) -> requests.Response:
    return requests.get(url)