from urllib.parse import urljoin

from Downloader import Downloader
from gameCrawler.lolCrawler import lolCrawler
from bs4 import BeautifulSoup


linkLolWiki = "https://lol.fandom.com/wiki"


def lolRequestHtml(link, league):
    return lolCrawler(link, league, Downloader()).getLolInformation(league)


def lolRequestStatusCode(link, league):
    return lolCrawler(link, league, Downloader()).getRequestStatus(league)


page = lolRequestHtml(linkLolWiki, "")
html_page = BeautifulSoup(page, 'html.parser')

listSearchAllUl = html_page.findAll('ul')
listSearchChampionships = listSearchAllUl[7]
listChampionship = [championship['href'].replace('/wiki/', '') for championship in listSearchChampionships.findAll('a')]
print(listChampionship[0])

print(lolRequestStatusCode(linkLolWiki, listChampionship[0]))
