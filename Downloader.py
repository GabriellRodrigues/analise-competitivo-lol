import requests


class Downloader:

    def __init__(self):
        self.seassion = requests.Session()

    def get(self, url, params=None):
        response = self.seassion.get(url, params=params, verify=False)
        response.raise_for_status()
        return response

    def post(self, url, data=None):
        response = self.seassion.post(url, data=data, verify=False)
        response.raise_for_status()
        return response

    def close(self):
        self.close()
