from lolRequestChampionships import lolChampionshipValues


linkLolWiki = "https://lol.fandom.com/wiki"

getRequestIntances = lolChampionshipValues(linkLolWiki)
championships = getRequestIntances.getLolChampionships()

print("Escolha o campeonato que deseja: ")
for index, leagues in enumerate(championships):
    print(f'\t{index+1} - {leagues.replace("_", " ")}')

championshipIndex = int(input("Entrada: "))

print(getRequestIntances.getLolTeamsOfChampionship(championshipIndex))
