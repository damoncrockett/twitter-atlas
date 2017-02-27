from PIL import Image
import pandas as pd
import numpy as np
import glob
import os

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR = BASEDIR + "image-slices/"
TARGET = BASEDIR + "polarhist/final/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

pad = 100

for i in range(len(city_table))[:64]:
    city = city_table.Center.iloc[i]
    CITYDIR = DIR + city + "/"
    yrs = [2012,2014]
    for yr in yrs:
        city_file = CITYDIR + str(yr) + ".csv"
        df = pd.read_csv(city_file)
        #df = df[df.width>15] not in data
        thumb_side = 16
        sortvar = 'val'
        
        def cratio(nbins):
            df['xbin'] = pd.cut(df.secpast,nbins,labels=False)
            bin_max = df.groupby('xbin').size().max()
            diff = 2*np.pi - float(nbins)/bin_max
            return diff
        
        midrange = int(round( len(df) / 233 )) # hardcoded ratio here
        
        if midrange - pad < 1:
            nbins = range(1, midrange + pad)   
        else:
            nbins = range(midrange - pad, midrange + pad) 
        
        cratios = [cratio(item) for item in nbins]
        diffs = [abs(item) for item in cratios]
        mindiff = diffs.index(min(diffs))
        nbins = nbins[mindiff]
        
        df['xbin'] = pd.cut(df.secpast,nbins,labels=False)
        bin_max = df.groupby('xbin').size().max()
        
        px_w = (bin_max * 2 * thumb_side) + thumb_side
        px_h = px_w
        
        canvas = Image.new('RGB',(px_w,px_h),'hsl(180,0%,100%)')
        
        def pol2cart(rho, phi):
            x = rho * np.cos(phi)
            y = rho * np.sin(phi)
            return(x, y)
        
        def bin2phi(binn):
            incr = float(360)/nbins
            return np.radians(incr*binn)
        
        def bin2phideg(binn):
            incr = float(360)/nbins
            return incr*binn
            
        bins = list(set(list(df.xbin)))
        bins.sort()
        
        for item in bins:   
            tmp = df[df.xbin==item]
            tmp.sort_values(by=sortvar,inplace=True,ascending=False)
            tmp.reset_index(drop=True,inplace=True)

            for j in range(len(tmp)):
                im = Image.open(tmp.local_path.loc[j])
                im = im.convert('RGBA')
                im.thumbnail((thumb_side,thumb_side),Image.ANTIALIAS)
                pos = bin_max - j
                xy = pol2cart(pos,bin2phi(item))
                phi = bin2phideg(item)
                im = im.rotate(phi,expand=1)
        
                xcoord = int(round((xy[0] + bin_max) * thumb_side))
                ycoord = int(round((bin_max - xy[1]) * thumb_side))
                canvas.paste(im,(xcoord,ycoord),im)
                
                print(city,yr,item,j)
                
        attr_str = str(yr)+"_"+str(len(df))+"_"+str(px_w)+"_"+str(nbins)
        canvas.save(TARGET+city+"_"+attr_str+".png") 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        