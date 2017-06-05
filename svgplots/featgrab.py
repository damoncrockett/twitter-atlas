import pandas as pd
import numpy as np
import sys

feat = sys.argv[1]

BASEDIR = "/data/damoncrockett/twitter-atlas/"
FOURDIR = BASEDIR + "image-slices-plus-plus-timestamp/"
TWODIR = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

yrs = [2012, 2014]

counter = -1
for city in city_table.Center:
    for yr in yrs:
        counter+=1
        print(str(counter),city,str(yr))

        if yr==2012:
            DDIR = TWODIR
        elif yr==2014:
            DDIR = FOURDIR

        df = pd.read_csv(DDIR + city + "_" + str(yr) + ".csv")
        df = df[[feat]]
        df['year'] = yr
        df['city'] = city

        if counter==0:
            tmp = df
        else:
            tmp = tmp.append(df)

tmp.to_csv(BASEDIR+feat+".csv",index=False)