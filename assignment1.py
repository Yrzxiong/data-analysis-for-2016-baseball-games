# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:35:33 2018

@author: Keddy
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Batting.csv')
df.head()
df.info()
playerInfo = df[['playerID','nameFirst','nameLast','birthYear']].drop_duplicates()
df['PA']=df['AB']+df['BB']+df['IBB']+df['SH']+df['SF']
df['OBP'] = (df['H']+df['BB']+df['IBB']+df['SH']+df['SF'])/df['AB']
df['Average'] = df['H']/df['AB']
#3) How many players have hit 40 or more HRs in one single season? (Number only)¶
g_SumSeason = df.groupby(['playerID', 'yearID'], as_index = False).sum()    # sort by player and season                                      # the sum of each season per player
len(g_SumSeason[g_SumSeason['HR']>=40])                            # the number of players who hit 40 or more HRs per season

#4) How many players have hit more than 600 HRs for their career? (Dataframe)
g_SumID = df.groupby('playerID', as_index = False).sum()                    # sort by player
g =g_SumID[g_SumID['HR']>600][['playerID','HR']]                   # players who hit more than 600 HRs for their career
g.columns = ['playerID','Total_HR']
pd.merge(playerInfo,g)

#5)	How many players have hit 40 2Bs, 10 3Bs,
# 200 Hits, and 30 HRs (inclusive) in one season? (Number Only)
len(g_SumSeason[(g_SumSeason['2B']>=40) & (g_SumSeason['3B']>=10) &(g_SumSeason['H']>=200) &(g_SumSeason['HR']>=30)])

#6)	How many players have had 100 or more SBs in a season? (Dataframe)
g = g_SumSeason[g_SumSeason['SB']>=100][['playerID','yearID']]
pd.merge(playerInfo,g)

#7)	How many players in the 1960s have hit more than 200 HRs? (Dataframe)
g_1960sHRs = g_SumSeason[(g_SumSeason['yearID']>=1960)& (g_SumSeason['yearID']<1970)].groupby('playerID',as_index = False).sum()[['playerID','HR']]
g = g_1960sHRs[g_1960sHRs['HR']>200]                              # players who had hit more than 200 HRs
g.columns = ['playerID','1960s_HRs']
pd.merge(playerInfo,g)

#8)	Who has hit the most HRs in history? (Dataframe)
g = g_SumID[g_SumID['HR'] == max(g_SumID['HR'])][['playerID','HR']]                    # player who had the most HRs
g.columns = ['playerID','Total_HRs']
pd.merge(playerInfo, g)

#9)	Who had the most hits in the 1970s? (Dataframe)
g_1970sHs = g_SumSeason[(g_SumSeason['yearID']>=1970)& (g_SumSeason['yearID']<1980)].groupby('playerID',as_index = False).sum()[['playerID','H']]
g = g_1970sHs[g_1970sHs['H']==max(g_1970sHs['H'])]                              # players who had hit more than 200 HRs
g.columns = ['playerID','1970s_Hs']
pd.merge(playerInfo,g)

#10)	Top 5 highest OBP (on base percentage) with at least 500 PAs in 1977?  (Dataframe)
g = g_SumSeason[(g_SumSeason['yearID'] == 1977) & (g_SumSeason['PA']>= 500)][['playerID','yearID','PA','OBP']]
pd.merge(playerInfo,g.sort_values('OBP')[-5:]).sort_values('OBP',ascending = False)

#11)	Top 8 highest averages in 2013 with at least 300 PAs? (Dataframe)
g = g_SumSeason[(g_SumSeason['yearID'] == 2013) & (g_SumSeason['PA']>= 300)][['playerID','yearID','PA','Average']]
pd.merge(playerInfo,g.sort_values('Average')[-8:]).sort_values('Average',ascending = False)

#12)	Leaders in hits from 1940 up to and including 1949. (Dataframe)
g = pd.DataFrame({'playerID' : []})
for i in np.arange(1940, 1950):
    g1 = g_SumSeason[g_SumSeason['yearID'] == i][['playerID','yearID','H']]
    g1 = g1[g1['H']==max(g1['H'])]
    g = g.append(g1)
pd.merge(playerInfo,g).sort_values('yearID')

#13)	Who led MLB with the most hits the most times?  And how many times?  (Dataframe, Number)

#14) Which players have played the most games for their careers? Top 5, descending by games played presented as a dataframe
g_SumID















