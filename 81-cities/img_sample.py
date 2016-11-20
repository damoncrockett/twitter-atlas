BASE = "/data/damoncrockett/twitter-atlas/"
IMGMD = BASE+"images-md/"
TARGET = BASE+"vis/"

n = 746

"""
This code produces an image sample from the Twitter Atlas data,
a collection of tweeted images from 2011-2014 across 81 world cities.
Every image in the sample comes from a unique user account, and there
are 746 images from each city (this was the lowest number of unique 
accounts amongst all 81 cities). The images are organized into circles
by city, and each circle is placed roughly where it stands geographically
relative to the others, although forced to a 9x9 grid. Images are sorted
within each circle by time, with the earliest images at the center and
getting later in time toward the periphery. The result is a quite large
single image, 36846x36846 pixels.
"""

import pandas as pd
from PIL import Image,ImageDraw
import numpy as np
from shapely.geometry import Point
from dateutil import parser

# our list of cities, with lat/lon
df = pd.read_csv(BASE+"city-list-count-10km-img.csv")

# flight and rank to fix city centers
df.sort_values(by="lon",inplace=True)
df["x_grid"] = np.repeat(np.arange(16,288,32),9)
df.sort_values(by=["x_grid","lat"],ascending=[True,False],inplace=True) # N.B. -lat
df["y_grid"] = list(np.arange(16,288,32)) * 9

df.reset_index(drop=True,inplace=True)

###-------------------
###   grid list
###-------------------

grid_side = 288

x,y = np.repeat(range(grid_side),grid_side),range(grid_side) * grid_side
grid_list = pd.DataFrame()
grid_list['x'] = x
grid_list['y'] = y
grid_list['x_bin'] = pd.cut(grid_list.x,bins=9,labels=False)
grid_list['y_bin'] = pd.cut(grid_list.y,bins=9,labels=False)
grid_list.sort_values(by=['x_bin','y_bin'],inplace=True)
grid_list['subcanvas'] = np.repeat(range(81),1024)

# make into shapely points
point = []
for i in grid_list.index:
    point.append(Point(grid_list.x.loc[i],grid_list.y.loc[i]))
grid_list['point'] = point

###-------------------
###   plotting loop
###-------------------

thumb_side = 128

px_w = thumb_side * grid_side
px_h = thumb_side * grid_side
canvas = Image.new("RGB",(px_w,px_h),(50,50,50))

for i in df.index:
    city = df.Center.loc[i]
    
    # subgrid by city to speed search
    subgrid = list(grid_list['point'][grid_list.subcanvas==i])
    
    # plot city name on canvas at 'city center'
    template = Image.new("RGB", (thumb_side, thumb_side), (50,50,50))
    draw = ImageDraw.Draw(template)    
    draw.text((5,thumb_side/2),city,fill="white") # hard-coded the left edge...
    
    x = df.x_grid.loc[i] * thumb_side
    y = df.y_grid.loc[i] * thumb_side   
    canvas.paste(template,(x,y))
    
    city_center = Point(df.x_grid.loc[i],df.y_grid.loc[i])
    subgrid.remove(city_center)
    
    # sampling one img from ea of 746 user accts
    print "sampling ",city
    
    citydf = pd.read_csv(IMGMD+city+".csv")
    actors = citydf.actor_id.unique()
    actors_sample = np.random.choice(actors,size=n,replace=False)
    
    idxs = []
    for actor in actors_sample:
        tmp = citydf[citydf.actor_id==actor]
        idx = np.random.choice(tmp.index,size=1,replace=False)
        idxs.append(int(idx))
    
    tmp = citydf.loc[idxs] # this is our sample
    
    print "parsing datetime..."
    
    tmp.postedTime = tmp.postedTime.apply(parser.parse)
    tmp.sort_values(by="postedTime",inplace=True)
    
    print "plotting images..."
    
    for j in tmp.index:
        im = Image.open(tmp.local_path.loc[j])
        im.thumbnail((thumb_side,thumb_side),Image.ANTIALIAS)
        
        closest_open = min(subgrid,key=lambda x: city_center.distance(x))
        x = int(closest_open.x) * thumb_side
        y = int(closest_open.y) * thumb_side
        canvas.paste(im,(x,y))
        subgrid.remove(closest_open)
        
        print i,city,j

canvas.save(TARGET+"smp.png")   