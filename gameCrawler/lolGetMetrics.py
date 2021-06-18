import requests
from bs4 import BeautifulSoup

request = requests.get('https://lol.fandom.com/wiki/PaiN_Gaming/Match_History').content

html = BeautifulSoup(request, 'html.parser')

soup = html.findAll('a', rel="nofollow noreferrer noopener", target="_blank")
lista1 = list()

for i in soup:
    #print(i.prettify())
    if "http://matchhistory.na.leagueoflegends.com/" in i['href']:
        lista1.append(i['href'])

request2 = requests.get(lista1[0]).content
html2 = BeautifulSoup(request2, "html.parser")
print(html2.prettify())

