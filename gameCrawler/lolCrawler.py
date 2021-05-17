import json
from urllib.parse import urljoin


class lolCrawler:
    def __init__(self, lol_url, championship, downloader):
        self.lol_url = lol_url
        self.downloader = downloader
        self.getLolInformation(championship)

    def getLolInformation(self, championship):
        lolUrl = urljoin(self.lol_url, f"/{championship}")
        params = self.configParams(championship)
        response = self.downloader.post(lolUrl, data=params)
        print(response)

    def configParams(self, championship):
        return {"name": championship}
