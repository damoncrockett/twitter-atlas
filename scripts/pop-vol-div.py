import pandas as pd
import glob,os
from dateutil import parser
import datetime
import pytz

DIR = "/data/damoncrockett/twitter-atlas/"
MDDIR = DIR + "images-md/"

tables = glob.glob(os.path.join(MDDIR,"*.csv"))
maxtime = datetime.datetime(2012,7,14,16,0,0,0,tzinfo=pytz.UTC)

cities = []
years = []
tweets = []
actors = []

yrs = [2012,2014]

for table in tables:
    city = os.path.basename(table)[:-4]
    df = pd.read_csv(table)
    df['postedTimeParsed'] = df.postedTime.apply(parser.parse)
    df['year'] = [item.year for item in df.postedTimeParsed]
    df = df[df.year.isin(yrs)]

    for yr in yrs:

        cities.append(city)
        years.append(yr)

        if yr==2014:
            tmp = df[df.year==yr]
            tweets.append(len(tmp))
            actors.append(len(tmp.actor_id.unique()))
        elif yr==2012:
            tmp = df[df.year==yr]
            tmp = tmp[tmp.postedTimeParsed <= maxtime]
            tweets.append(len(tmp))
            actors.append(len(tmp.actor_id.unique()))

        print(city,yr,len(tmp),len(tmp.actor_id.unique()))

datatable = pd.DataFrame({
    "city":cities,
    "year":years,
    "tweets":tweets,
    "actors":actors
    })

datatable.to_csv("pop-vol-div.csv",index=False)