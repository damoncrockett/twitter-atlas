import pandas as pd
import glob
import os
from dateutil import parser

DIR = "/data/damoncrockett/twitter-atlas/"
TARGET = DIR+"city-tables-wide-combined/"
DATA = DIR+"city-tables-wide/"
CITIES = pd.read_csv(DIR+"city-list.csv")

all_files = glob.glob(os.path.join(DATA,"*.csv"))

city_lens = []
city_counter=0
for city in CITIES.Center:
    city_counter+=1
    city_files = [item for item in all_files if city in item]
    counter=0
    for city_file in city_files:
        tmp = pd.read_csv(city_file)
        counter+=1
        if counter==1:
            df = tmp
        else:
            df = df.append(tmp)
    df.postedTime = df.postedTime.apply(parser.parse)
    df.sort("postedTime",inplace=True)
    city_lens.append(len(df))
    df.to_csv(TARGET+city+".csv",index=False)
    print city_counter
    
CITIES['total_tweets'] = city_lens
CITIES.to_csv("./city-list-count.csv",index=False)    