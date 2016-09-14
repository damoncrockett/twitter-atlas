import shapefile
DIR = "/data/damoncrockett/Twitter_Global_Viz/"
FILE = "TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp"
polygons_sf = shapefile.Reader(DIR+FILE)
records = polygons_sf.records()
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]

# World country polygons from ThematicMapping.org, 
# argued to be the best free world shapefile by this analysis:
# http://barendgehrels.blogspot.com/2010/12/free-shapefile-of-countries-of-world.html

country_names = [item[4] for item in records]

from shapely.geometry import Point, Polygon
polygon_list = [Polygon(item) for item in polygon_points]

from rtree import index
idx = index.Index()
count = -1
for item in polygon_list:
    count +=1
    idx.insert(count, item.bounds)
    
import sys
YEAR = sys.argv[1]
START = sys.argv[2]
STOP = sys.argv[3]
FOLDER = "/data/damoncrockett/"+str(YEAR)+"/"

import pandas as pd

for chunk_num in range(int(START),int(STOP)+1):
	filestring = FOLDER+"output_"+str(YEAR)+"_chunk_"+str(chunk_num)+".csv"

	df = pd.read_csv(filestring)
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
	
	df['country_computed'] = country
	df.to_csv(filestring,index=False)