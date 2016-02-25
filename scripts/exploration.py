# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:54:41 2016

@author: jmf
"""

import pandas as pd
import numpy as np
from os import mkdir
from os.path import isdir


replacements    = [
                    ["northern","n"],
                    ["eastern","e"],
                    ["southern","s"],
                    ["western","w"],
                    ["north","n"],
                    ["east","e"],
                    ["south","s"],
                    ["west","w"]

                    ]

def getGames():
    gamesFrame  = pd.read_csv(folder+"RegularSeasonCompactResults.csv")
    recent      = gamesFrame[gamesFrame["Season"]>2002]
    return recent


def getTeams():
    teamsFrame  = pd.read_csv(folder+"Teams.csv")
    #print teamsFrame        
    #teamNames   = teamsFrame["Team_Name"]
    return teamsFrame
        
        
def getPom():
    pomFrame    = pd.read_csv(folder+"kenpom.csv")
    pomNames    = pomFrame["Team"]
    #print pomFrame.head()
    return pomNames
    
def teams2pom(teams,pomSyn,games):
    teamMap     = {}
    ids1        = set(games["Wteam"].values.tolist())
    ids2        = set(games["Lteam"].values.tolist())
    teamIDs     = set(ids1|ids2)
    matches = 0
    missingTeams = 0
    
    idToPom     = {}
    for tid in teamIDs:
        team    = teams[teams["Team_Id"]==tid]["Team_Name"].values[0]
        if team in pomSyn:
            idToPom[tid] = pomSyn[team]
            matches+=1
        else:
            idToPom[tid] = team+"\t"+"WRONG" 
            missingTeams+=1

    print matches, missingTeams
    with open("pomMap.txt",'wb') as f:    
        for k,v in idToPom.iteritems():
            f.write(str(k)+"\t"+str(v)+"\n")
    
folder  = "data/"
#teams   = getTeams().tolist()
pomNames     = getPom().tolist()
pomSyn  = {}
pom     = []
for p in pomNames:
    n = p.lower().replace(" ",'').replace('.','').replace(' ','').replace("'",'')
    pomSyn[n]   = p
    for rep in replacements:
        n   = n.replace(rep[0],rep[1])
    pomSyn[n]   = p

teams   = getTeams()
teams["Team_Name"] = teams["Team_Name"].apply(lambda x: x.lower().strip().replace(" ",'').replace('.','').replace("'",''))

print pomSyn
games   = getGames()
match   = teams2pom(teams,pomSyn,games)



        
#print matches, missingTeams