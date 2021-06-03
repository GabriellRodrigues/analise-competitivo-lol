from urllib.parse import urljoin


class lolCrawler:
    def __init__(self, lol_url, championship, downloader):
        self.lol_url = lol_url
        self.downloader = downloader
        self.championship = championship

    def getLolInformation(self):
        lolUrl = urljoin(self.lol_url, f"/{self.championship}")
        response = self.downloader.get(lolUrl).content
        return response

    def getRequestStatus(self):
        lolUrl = urljoin(self.lol_url, f"/{self.championship}")
        response = self.downloader.get(lolUrl).status_code
        return response
