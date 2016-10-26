BASEDIR = "/data/damoncrockett/twitter-atlas/"
CITYDIR = BASEDIR + "city-tables/"
CITYDIRWIDE = BASEDIR + "city-tables-wide/"
TWEETDIR = BASEDIR + "tweets/"

import sys
year = sys.argv[1]

import os
import glob

tweet_tables = glob.glob(os.path.join(TWEETDIR,"*.csv"))
tweet_filelist = list(tweet_tables)
tweet_files = [item for item in tweet_filelist if year in item]

city_tables = glob.glob(os.path.join(CITYDIR,"*.csv"))
city_filelist = list(city_tables)
city_files = [item for item in city_filelist if year in item]

import pandas as pd

city_counter = 0    
for city_file in city_files:
    city_counter+=1
    basename = os.path.basename(city_file)
    city_df = pd.read_csv(city_file)
    ids = list(city_df.mongo_id)
    
    chunk_counter = 0
    for tweet_file in tweet_files:
        chunk_counter+=1
        tmp = pd.read_csv(tweet_file)
        tmp = tmp[tmp.mongo_id.isin(ids)]
        if chunk_counter==1:
            df = tmp
        else:
            df = df.append(tmp)
        print city_counter,chunk_counter
            
    df.set_index("mongo_id",inplace=True)
    city_df = city_df.join(df,on="mongo_id")
    city_df.to_csv(CITYDIRWIDE + basename,index=False)