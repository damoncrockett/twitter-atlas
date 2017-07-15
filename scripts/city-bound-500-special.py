import pandas as pd
import numpy as np

PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TWEETDIR = DIR + "tweets/"
TARGET = DIR + "500-city-tables-10km/"
DATA = pd.read_csv(DIR + "world_ua_bboxes.csv")

tweettables = [
    "twitter_metadata_2011.csv",
    "twitter_metadata_2012.csv",
    "twitter_metadata_2013.csv",
    "twitter_metadata_2014_mezzo.csv",
]

# 1 degree latitude = 110.574 km
# 1 degree longitude = 111.320 * cos(latitude) km
# And make sure we use radians when computing cosine!

lat_margin = 5 / 110.574 #bc we want 10km box
def lon_margin(lat):
    margin = 5 / ( 111.320 * np.cos( np.radians(lat) ) )
    return margin

for tweettable in tweettables:
    year = tweettable.split("_")[2][:-4]

    df = pd.read_csv(PRE + tweettable)
    df = df[['mongo_id','lat','lon','postedTime']]

    for i in [38,315]:

        city = DATA.Center.loc[i]
        lon = DATA.lon.loc[i]
        lat = DATA.lat.loc[i]

        lat_min = lat - lat_margin
        lat_max = lat + lat_margin
        lon_min = lon - lon_margin(lat)
        lon_max = lon + lon_margin(lat)

        tmp = df[df.lat > lat_min]
        tmp = tmp[tmp.lat < lat_max]
        tmp = tmp[tmp.lon > lon_min]
        tmp = tmp[tmp.lon < lon_max]

        print(year,i,city)

        tmp.to_csv(TARGET+city+"_"+year+".csv",index=False)
        
