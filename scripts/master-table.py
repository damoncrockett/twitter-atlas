import pandas as pd 
import glob,os
from dateutil import parser

PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TABLEDIR = DIR + "500-city-tables-10km-wide"
DATA = DIR + "world_ua_bboxes.csv"

df = pd.read_csv(DATA)
df = df[['Center','Urban_Area','Country','lat','lon']]

cities = df.Center
years = range(2011,2015)
months = range(1,13)
measures = ['tweet','actor']

cols = []
for measure in measures:
    for year in years:
        for month in months:
            cols.append(measure+str(year)+str(month))

cols = cols[:43] # bc we only have into July 2014
X = pd.DataFrame(index=cities,columns=cols)

for city in X.index:
    for year in years:
        
        # hack bc I'm dumb
        if year==2014:
            yearstring = ''
        else:
            yearstring = str(year)

        tablestr = TABLEDIR + city + "_" + yearstring + ".csv"
        table = pd.read_csv(tablestr)

        table.postedTime = table.postedTime.apply(parser.parse)
        table['month'] = [item.month for item in table.postedTime]

        for month in months:
            tmp = table[table.month==month]

            for measure in measures:
                
                if measure=='tweet':
                    X.loc[city,measure+str(year)+str(month)] = len(tmp)
                elif measure=='actor':
                    X.loc[city,measure+str(year)+str(month)] = len(tmp.actor_id.unique())

df = df.join(X,on="Center")
df.to_csv(DIR+"master-table-500.csv",index=False)