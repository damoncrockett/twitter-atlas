BASEDIR = "/data/damoncrockett/twitter-atlas/"
CITYDIR = BASEDIR + "city-tables/"
CITYDIRWIDE = BASEDIR + "city-tables-wide/"
TWEETDIR = BASEDIR + "tweets/"

import sys
year = sys.argv[1]

import os
import glob

city_tables = glob.glob(os.path.join(CITYDIR,"*.csv"))
city_filelist = list(city_tables)

city_files = [item for item in city_filelist if item.split("_")[1].rstrip(".csv")==year]

all_tweets_table = TWEETDIR + "twitter_metadata_" + year + "_rich.csv"

import pandas as pd
all_tweets = pd.read_csv(all_tweets_table)
all_tweets.set_index("mongo_id",inplace=True)

counter = 0    
for city_file in city_files:
    counter+=1
    basename = os.path.basename(city_file)
    df = pd.read_csv(city_file)
    df = df.join(all_tweets,on="mongo_id")
    df.to_csv(CITYDIRWIDE + basename,index=False)
    print counter