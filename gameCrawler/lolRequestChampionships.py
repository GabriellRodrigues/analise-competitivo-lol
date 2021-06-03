from gameCrawler.lolRequests import getRequests


class lolChampionshipValues:
    def __init__(self, link):
        self.link = link

    def getLolChampionships(self):
        listSearchAllUl = getRequests(self.link, "").lolRequestSoup().findAll('ul')
        listSearchChampionships = listSearchAllUl[7]
        listChampionship = [championship['href'].replace('/wiki/', '') for championship in listSearchChampionships.findAll('a')]
        listChampionship.remove('Roster_Swaps/Current/North_America')
        listChampionship.remove('Match_History_Index')

        return listChampionship

    def getLolTeamsOfChampionship(self, championshipIndex):
        getChampionshipHtml = getRequests(self.link, self.getLolChampionships()[championshipIndex - 1]).lolRequestSoup()
        teamsTag = getChampionshipHtml.findAll('a', class_='catlink-teams tWACM tWAFM tWAN to_hasTooltip')
        teams = [i.get_text() for i in teamsTag]

        return teams
