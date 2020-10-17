import requests


class Client(object):

    def __init__(self, base_url: str):
        self._base_url = base_url

    def get(self, endpoint: str):
        return requests.get(self._base_url + endpoint).json()
