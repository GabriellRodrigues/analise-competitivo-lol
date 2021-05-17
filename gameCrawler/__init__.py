from Downloader import Downloader
from lolCrawler import lolCrawler


class Championship(lolCrawler):
    def __init__(self, championship):
        super().__init__("https://lol.fandom.com/wiki/", championship, Downloader())
