class InstrumentsConfiguration(object):
    def __init__(self, start_year: int, api_url: str):
        self._start_year = start_year
        self._api_url = api_url

    @property
    def start_year(self) -> int:
        return self._start_year

    @property
    def api_url(self) -> str:
        return self._api_url
