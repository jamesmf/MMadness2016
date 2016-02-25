import pandas as pd
import numpy as np
from os import mkdir
from os.path import isdir


class Team():
    
    def __init__(self,ID,year):
        self.ID     = ID
        self.year   = int(year)
        self.name   = self.IDtoName()
        self.games  = self.getGames()
        self.stats  = self.getStats()
        
    def IDtoName(self):
        return IDtoPom[self.ID]
        
        
    def getGames(self):
        gy  = games[games["Season"] == self.year]
        Ws  = gy[gy["Wteam"] == self.ID]
        Ls  = gy[gy["Lteam"] == self.ID]
        gs  = pd.concat((Ws,Ls))
        return gs
 
    def getStats(self):
        py  = pom[pom["Year"] == self.year]
        return py[py["Team"] == self.name]       
        
def getIDtoPom():
    with open("../fullPomMap.csv",'rb') as f:
        l   = [x for x in f.read().split("\n") if x != '']
    IDtoPom     = {}
    for row in l:
        s   = row.split(",")
        IDtoPom[int(s[0])] = s[1]
    return IDtoPom
        
games   = pd.read_csv("../data/RegularSeasonDetailedResults.csv")
pom     = pd.read_csv("../data/kenpom.csv")
pom["Team"]     = pom["Team"].apply(lambda x: x.strip())
IDtoPom = getIDtoPom()


myTeam  = Team(1421,2003)
print myTeam.name
print myTeam.stats