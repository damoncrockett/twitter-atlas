DIR = "/data/damoncrockett/twitter-atlas/"
STDIR = DIR + "spacetime/"
prefix = "spacetime_"

import pandas as pd 
from dateutil import parser
import datetime

def teparse(dt):
    try:
        return parser.parse(dt)
    except:
        return "err"

def pTsubset(df):
    try:
        return df[df.postedTime!="err"]
    except:
        return df

df = pd.read_csv(STDIR+prefix+"2011.csv")
df.postedTime = df.postedTime.apply(teparse)
df = pTsubset(df)

t0 = df.postedTime.min()
delta = datetime.timedelta(days=7)
nweeks = 150 # fact about our data

weeklist = []
lbound = t0
for i in range(nweeks):
    rbound = lbound + delta
    weeklist.append((lbound, rbound))
    lbound = rbound

df['week'] = 0
for i in range(len(weeklist)):
    lbound = weeklist[i][0]
    rbound = weeklist[i][1]

    tmp = df[df.postedTime >= lbound]
    tmp = tmp[tmp.postedTime < rbound]
    idxs = tmp.index
    df.week.loc[idxs] = i

df = df[['week','lat','lon']]
df.to_csv(STDIR+prefix+"2011_week.csv",index=False)

for year in ["2012","2013","2014"]:
    df = pd.read_csv(STDIR+prefix+year+".csv")
    df.postedTime = df.postedTime.apply(teparse)
    df = pTsubset(df)
    
    df['week'] = 0
    for i in range(len(weeklist)):
        lbound = weeklist[i][0]
        rbound = weeklist[i][1]

        tmp = df[df.postedTime >= lbound]
        tmp = tmp[tmp.postedTime < rbound]
        idxs = tmp.index
        df.week.loc[idxs] = i
        print(year,i)

    df = df[['week','lat','lon']]
    df.to_csv(STDIR+prefix+year+"_week.csv",index=False)