#Dylan Miller

#This program will convert sports records into league
#rankings and can return the win, loss, draw record of a given team

class Team:
    """Team class takes in a team name and will track their
    wins, losses, and draws"""
    def __init__(self,name):
        "Creates the team using the team name"
        self.name = name
        self.teamWins = 0
        self.teamDraws = 0
        self.teamLosses = 0
        
    def addWin(self):
        "Accumulates total wins"
        self.teamWins = self.teamWins + 1
        return self.teamWins

    def addDraw(self):
        "Accumulates total draws"
        self.teamDraws = self.teamDraws + 1
        return self.teamDraws

    def addLoss(self):
        "Accumulates total losses"
        self.teamLosses = self.teamLosses + 1
        return self.teamLosses

    def getName(self):
        "Returns the name of the team"
        return self.name

    def getWins(self):
        "Returns the total wins"
        return self.teamWins

    def getDraws(self):
        "Returns the total draws"
        return self.teamDraws

    def getLosses(self):
        "Returns the total losses"
        return self.teamLosses

    #returns the full record of the team
    def __str__(self):
        return str(self.teamWins)+", "+str(self.teamDraws)+", "+str(self.teamLosses)

def main():
    #gets file name
    file = str(input("Sports league file name: "))
    file = open(file,"r")
    #saves the name of the sports league for the ranking table
    leagueName = file.readline()
    #adds all teams to a dictionary using the team name as a key that returns
    #the corresponding class object
    dictTeams = {}
    name = file.readline()[:-1]
    while name != "":
        dictTeams[name] = Team(name)
        name = file.readline()[:-1]
    #saves each of the games as an item in a list
    games = file.readlines()
    for i in range (len(games)):
        split = games[i]
        #finds the scores of each team
        split = split.split(" ")
        score1 = split.index("vs") - 1
        score1 = split[score1]
        score2 = split[-1]
        score2 = score2[:-1]
        #checks for which team won and adds a win, loss, or draw
        #to the corresponding class object
        if score1 > score2:
            #finds the first team's name
            teamName = " ".join(split[0:split.index("vs") - 1])
            dictTeams[teamName].addWin()
            #finds the second team's name
            teamName = " ".join(split[split.index("vs") + 1:-1])
            dictTeams[teamName].addLoss()
        elif score1 < score2:
            teamName = " ".join(split[0:split.index("vs") - 1])
            dictTeams[teamName].addLoss()
            teamName = " ".join(split[split.index("vs") + 1:-1])
            dictTeams[teamName].addWin()
        elif score1 == score2:
            teamName = " ".join(split[0:split.index("vs") - 1])
            dictTeams[teamName].addDraw()
            teamName = " ".join(split[split.index("vs") + 1:-1])
            dictTeams[teamName].addDraw()
    #moves all the team objects to a list for sorting
    teams = []
    for i in dictTeams.values():
        teams = teams + [i]
    #sorts alphabetically first then by value (greatest to least amount of wins)
    teams.sort(key = Team.getName)
    teams.sort(reverse = True,key = Team.getWins)
    while True:
        menu = int(input(("\n1. Team stats\n2. League ranking\n3. Quit\n\n> ")))
        if menu == 1:
            #gets the team name (key) and checks for the object (value) associated
            teamName = str(input("\nWhat is the name of your team? "))
            teamName = dictTeams.get(teamName)
            #prints the wins, losses, and draws stored in the team
            print("\nWins: "+str(teamName.getWins()))
            print("Draws: "+str(teamName.getDraws()))
            print("Losses: "+str(teamName.getLosses()))
        elif menu == 2:
            #prints the title of the sports league
            print("\n"+leagueName[:-1]+" Ranking\n")
            print("Team\t\tW\tD\tL")
            print("----\t\t-\t-\t-")
            #prints the name, wins, losses, and draws for each team
            for i in range (len(teams)):
                print(str(teams[i].getName()),end="\t")
                print(str(teams[i].getWins()),end="\t")
                print(str(teams[i].getDraws()),end="\t")
                print(str(teams[i].getLosses()))
        elif menu == 3:
            #terminates the loop once the user selects to quit
            break
        else:
            print("sorry that is not a valid response.")
main()
