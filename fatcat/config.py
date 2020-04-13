class Config:

    def __init__(self):
        with open('fmp_api_key.txt', 'r') as f:
            self._api_key = f.read()
        self._dbpath = 'db/fatcat.db'

    @property
    def api_key(self):
        return self._api_key

    @property
    def dbpath(self):
        return self._dbpath


config = Config()
