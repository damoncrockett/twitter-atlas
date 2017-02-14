import pandas as pd
import numpy as np

DIR = "/data/damoncrockett/twitter-atlas/"
TARGET = DIR+"city-tables-wide-combined-10km/"
DATA = DIR+"city-tables-wide-combined/"
CITIES = DIR+"city-list-count.csv"

# 1 degree latitude = 110.574 km
# 1 degree longitude = 111.320 * cos(latitude) km
# And make sure we use radians when computing cosine!

lat_margin = 5 / 110.574 #bc we want 10km box
def lon_margin(lat):
    margin = 5 / ( 111.320 * np.cos( np.radians(lat) ) )
    return margin

city_list = pd.read_csv(CITIES)
city_lens = []
for i in range(len(city_list)):
    city = city_list.Center.loc[i]
    lon = city_list.lon.loc[i]
    lat = city_list.lat.loc[i]
    
    filestring = DATA+city+".csv"
    tmp = pd.read_csv(filestring)
    
    lat_min = lat - lat_margin
    lat_max = lat + lat_margin
    lon_min = lon - lon_margin(lat)
    lon_max = lon + lon_margin(lat)
    
    tmp = tmp[tmp.lat > lat_min]
    tmp = tmp[tmp.lat < lat_max]
    tmp = tmp[tmp.lon > lon_min]
    tmp = tmp[tmp.lon < lon_max]
    
    city_lens.append(len(tmp))    
    
    tmp.to_csv(TARGET+city+".csv",index=False)
    
    print i+1
    
city_list['total_tweets'] = city_lens
city_list.to_csv("./city-list-count-10km.csv",index=False)