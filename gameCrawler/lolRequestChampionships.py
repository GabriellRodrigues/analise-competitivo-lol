from gameCrawler.lolRequests import getRequests


class lolChampionshipValues:
    def __init__(self, link):
        self.link = link

    def getLolChampionships(self):
        listSearchAllUl = getRequests(self.link, "").lolRequestSoup().findAll('ul')
        listSearchChampionships = listSearchAllUl[7]
        listChampionship = [championship['href'].replace('/wiki/', '') for championship in
                            listSearchChampionships.findAll('a')]
        listChampionship.remove('Roster_Swaps/Current/North_America')
        listChampionship.remove('Match_History_Index')

        return listChampionship

    # TODO usar set
    def duplicateItensRemove(self, listDuplicate):
        li = []
        for i in listDuplicate:
            if i not in li:
                li.append(i)

        return li

    def getLolTeamsOfChampionship(self, championshipIndex):
        getChampionshipHtml = getRequests(self.link, self.getLolChampionships()[championshipIndex - 1]).lolRequestSoup()
        teamsTag = getChampionshipHtml.findAll('a', class_='catlink-teams tWACM tWAFM tWAN to_hasTooltip')
        teamsElements = [i.get_text() for i in teamsTag]
        team = self.duplicateItensRemove(teamsElements)

        return team

    # TODO pegar os times da academy
    def getPlayersOfTeam(self, championshipIndex, teamIndex):
        prepareTeamString = self.getLolTeamsOfChampionship(championshipIndex)[teamIndex - 1].replace(' ', '_')
        getTeamHtml = getRequests(self.link, prepareTeamString).lolRequestSoup()
        playerElement = getTeamHtml.findAll('td', class_='team-members-player')
        playerslist = [player['data-player-id'] for player in playerElement]
        players = self.duplicateItensRemove(playerslist)

        return players

    # TODO remover este metódo
    def printListElement(self, listElement):
        for index, element in enumerate(listElement):
            print(f'\t{index + 1} - {element.replace("_", " ")}')
