import pandas as pd
import math
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR = BASEDIR + "image-slices/"
SAVEDIR = BASEDIR + "image-slices-plus/"
TARGET = BASEDIR + "huepeak/plots/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

for i in range(len(city_table)):
    city = city_table.Center.iloc[i]
    CITYDIR = DIR + city + "/"
    yrs = [2012,2014]
    for yr in yrs:
        city_file = CITYDIR + str(yr) + ".csv"
        df = pd.read_csv(city_file)

        r_all = int(math.ceil(np.sqrt(len(df)/np.pi)))
        phibins_all = int(math.ceil( len(df) / r_all ))
        print(city,yr,phibins_all)