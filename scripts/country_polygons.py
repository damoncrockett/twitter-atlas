import shapefile
DIR = "/data/damoncrockett/Twitter_Global_Viz/"
FILE = "world_country/world_country.shp"
polygons_sf = shapefile.Reader(DIR+FILE)
records = polygons_sf.records()
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]

country_names = [item[5] for item in records]

from shapely.geometry import Point, LinearRing
polygon_list = [LinearRing(item) for item in polygon_points]

from rtree import index
idx = index.Index()
count = -1
for item in polygon_list:
    count +=1
    idx.insert(count, item.bounds)
    
#import sys
#FILE = sys.argv[1]
#YEAR = sys.argv[2]
#FOLDER = DIR+"country"+str(YEAR)+"/"

FILE = "/data/damoncrockett/2011/output_2011.csv"

import pandas as pd
df = pd.read_csv(FILE)
n = len(df)

country = []
for i in range(n):
    print i
    tmp = "unplaced"
    point = (df.lon[i],df.lat[i])
    for j in idx.intersection(point):
        if Point(point).within(polygon_list[j]):
            tmp = country_names[j]
            break
    country.append(tmp)
    
df['country_computed_cw'] = country
df.to_csv(DIR+"twitter_metadata_11_country_computed_cw.csv",index=False)