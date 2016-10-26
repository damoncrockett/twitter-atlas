import pandas as pd
PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TARGET = DIR + "city-tables/"
DATA = pd.read_csv(DIR + "city-list.csv")

filestrings = [
"twitter_metadata_2011.csv",
"twitter_metadata_2012.csv",
"twitter_metadata_2013.csv",
"twitter_metadata_2014_mezzo.csv"
]

yrs = ["2011","2012","2013","2014"]

for j in range(len(yrs)):
    
    filestring = filestrings[j]
    yr = yrs[j]
    
    df = pd.read_csv(PRE+filestring)
    
    if yr!="2011": # bc 2011 does not have all these cols; have to requery it
        df = df[['mongo_id','lon','lat','postedTime','media_url']]
    
    for i in range(len(DATA)):
        
        city = DATA.Center.loc[i]
        lon = DATA.lon.loc[i]
        lat = DATA.lat.loc[i]
        
        tmp = df[df.lon > lon - 1]
        tmp = tmp[tmp.lon < lon + 1]
        tmp = tmp[tmp.lat > lat - 1]
        tmp = tmp[tmp.lat < lat + 1]
        
        print yr,city,i
        
        tmp.to_csv(TARGET+city+"_"+yr+".csv",index=False)
        