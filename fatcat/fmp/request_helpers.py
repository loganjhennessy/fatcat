import functools
from typing import Dict

import requests

from fatcat.config import config
from fatcat.db import get_db_conn


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
                return cache_results['response']
        return get_wrapper
    return decorator_check_cache


def check_cache_func(url):
    con = get_db_conn()
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM request_cache where url = ?", (url,))

    return cur.fetchone()


def cache_response_func(url, response):
    con = get_db_conn()
    cur = con.cursor()

    with con:
        cur.execute("INSERT INTO request_cache VALUES (?, ?)", (url, response))


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