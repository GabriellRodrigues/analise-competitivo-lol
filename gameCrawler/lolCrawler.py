from urllib.parse import urljoin


class lolCrawler:
    def __init__(self, lol_url, downloader):
        self.lol_url = lol_url
        self.downloader = downloader

    def getLolInformation(self, championship):
        lolUrl = urljoin(self.lol_url, f"/{championship}")
        response = self.downloader.get(lolUrl).content
        return response

    def getRequestStatus(self, championship):
        lolUrl = urljoin(self.lol_url, f"/{championship}")
        response = self.downloader.get(lolUrl).status_code
        return response
