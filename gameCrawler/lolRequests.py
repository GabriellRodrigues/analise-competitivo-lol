from lolCrawler import lolCrawler
from Downloader import Downloader
from bs4 import BeautifulSoup


class getRequests:
    def __init__(self, url, championship):
        self.url = url
        self.championship = championship

    def lolRequestHtml(self):
        return lolCrawler(self.url, self.championship, Downloader()).getLolInformation()

    def lolRequestStatusCode(self):
        return lolCrawler(self.url, self.championship, Downloader()).getRequestStatus()

    def lolRequestSoup(self):
        page = self.lolRequestHtml()
        soup = BeautifulSoup(page, 'html.parser')
        return soup
