from lolRequestChampionships import lolChampionshipValues


linkLolWiki = "https://lol.fandom.com/wiki"

getRequestIntances = lolChampionshipValues(linkLolWiki)

championships = getRequestIntances.getLolChampionships()
getRequestIntances.printListElement(championships)
championshipIndex = int(input("Entrada: "))

teams = getRequestIntances.getLolTeamsOfChampionship(championshipIndex)
getRequestIntances.printListElement(teams)
teamIndex = int(input("Entrada: "))

print(getRequestIntances.getPlayersOfTeam(championshipIndex, teamIndex))
