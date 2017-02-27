from PIL import Image
import pandas as pd
import numpy as np
import glob
import os

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR = BASEDIR + "image-slices/"
TARGET = BASEDIR + "polarscat/plots/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

def pol2cart(rho,phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)    

grid_side = 256 # derived from median city's img count
radius = grid_side / 2
secperweek = 604800

for i in range(len(city_table))[:64]:
    city = city_table.Center.iloc[i]
    CITYDIR = DIR + city + "/"
    yrs = [2012,2014]
    for yr in yrs:
        city_file = CITYDIR + str(yr) + ".csv"
        df = pd.read_csv(city_file)
        
        #thumb_side = 16
        thumb_side = 8
        sortvar = 'val'
        
        px_w = grid_side * thumb_side
        px_h = px_w
        
        canvas = Image.new('RGB',(px_w,px_h),(100,100,100))
        
        for j in df.index:
            im = Image.open(df.local_path.loc[j])
            im = im.convert('RGBA')
            im.thumbnail((thumb_side,thumb_side),Image.ANTIALIAS)
            
            secpast = df.secpast.loc[j]
            val = df.val.loc[j]
            phi = ( secpast / float(secperweek) ) * 360 
            rho = val * float(radius) # based on grid_side
            
            xy = pol2cart( rho, np.radians(phi) )
            im = im.rotate(phi,expand=1)
    
            xcoord = int(round((xy[0] + radius) * thumb_side))
            ycoord = int(round((radius - xy[1]) * thumb_side))
            canvas.paste(im,(xcoord,ycoord),im)
            
            print(city,yr,j,"of",len(df))
                
        attr_str = str(yr)+"_"+str(len(df))
        canvas.save(TARGET+city+"_"+attr_str+".png") 
        
        
        
        
        