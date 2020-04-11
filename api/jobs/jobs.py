import functools
import pickle
import sqlite3
from typing import Dict, List

import requests


sqlite3.register_converter("pickle", pickle.loads)
sqlite3.register_adapter(requests.Response, pickle.dumps)


class Config:

    def __init__(self):
        with open('api_key.txt', 'r') as f:
            self._api_key = f.read()

    @property
    def api_key(self):
        return self._api_key


config = Config()


class FMPRequestConfig():

    URL_TEMPLATE = '{protocol}://{host}/{api_version}/{endpoint}'

    def __init__(self, endpoint):
        self._protocol = 'https'
        self._host = 'fmpcloud.io'
        self._api_version = 'api/v3'
        self._endpoint = ''
        self._symbol = ''

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def symbol(self) -> str:
        return self._symbol

    def get_url(self) -> str:
        return self.URL_TEMPLATE.format(
            protocol=self._protocol,
            host=self._host,
            api_version=self._api_version,
            endpoint=self.endpoint
        )





def is_cached() -> bool:
    pass


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
    con = sqlite3.connect('db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM request_cache where url = ?", (url,))

    response = cur.fetchone()
    if not response:
        con.close()
    else:
        print('Cached response available, retrieving cached response')
        response = response['response']
        con.close()
    return response


def cache_response_func(url, response):
    con = sqlite3.connect('db/fatcat.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    with con:
        # cur.execute("INSERT INTO request_cache VALUES (?, ?)", (url, pickle.dumps(response)))
        cur.execute("INSERT INTO request_cache VALUES (?, ?)", (url, response))

    con.close()


def make_prepped_url(url: str, params: Dict[str, str]={}) -> str:
    print(params)
    params['apikey'] = config.api_key
    request = requests.Request(
        url=url,
        params=params
    )
    return request.prepare().url


@check_cache(check_cache_func, cache_response_func)
def make_request(url: str) -> requests.Response:
    return requests.get(url)


def get_symbol_list() -> List[Dict]:
    symbol_list_url = 'https://fmpcloud.io/api/v3/stock/list'
    prepped_url = make_prepped_url(symbol_list_url)
    response = make_request(prepped_url)
    return response.json()


def get_company_profile(symbol) -> Dict:
    pass


def get_companies():
    for symbol in get_symbol_list():
        company_profile = get_company_profile(symbol)


def main():
    symbol_list = get_symbol_list()
    print(len(symbol_list))


if __name__ == '__main__':
    main()