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
