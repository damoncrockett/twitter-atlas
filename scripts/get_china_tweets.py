import pandas as pd

df = pd.read_csv("./china_points.csv")

polygon_points = []
for i in range(len(df)):
    tup = [df.lon.loc[i],df.lat.loc[i]]
    polygon_points.append(tup)

from shapely.geometry import Point, Polygon
polygon_list = [Polygon(polygon_points)]

from rtree import index
idx = index.Index()
count = -1
for item in polygon_list:
    count +=1
    idx.insert(count, item.bounds)

import glob
import os
DIR = "/data/damoncrockett/2014/"

counter = -1
for file in glob.glob(os.path.join(DIR,"*.csv")):
    counter+=1
    tweets = pd.read_csv(file)
    m = len(tweets)
    countries = []
    for i in range(m):
        print counter,i
        tmp = 'outside'
        pt = (tweets.lon[i],tweets.lat[i])
        for j in idx.intersection(pt):
            if Point(pt).within(polygon_list[j]):
                tmp = "china"
                break
        countries.append(tmp)
    
    tweets['country'] = countries
    tweets_china = tweets[tweets.country=='china']
    
    if counter==0:
        d = tweets_china
    else:
        d = d.append(tweets_china)

d.to_csv("./china_2014.csv",index=False)
