from Downloader import Downloader
from gameCrawler.lolCrawler import lolCrawler


def testLolSearchChampionship():
    crawler = lolCrawler("https://lol.fandom.com/wiki", "CBLOL", Downloader())
