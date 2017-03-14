from PIL import Image
import pandas as pd
import numpy as np
import glob
import os
from skimage.io import imread
from skimage import color
from sklearn.neighbors import KernelDensity
import math

thumb_side = 8

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR = BASEDIR + "image-slices/"
SAVEDIR = BASEDIR + "image-slices-plus/"
TARGET = BASEDIR + "huepeak/plots/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

def pol2cart(rho,phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)   

def bin2phi(binn):
    incr = float(360)/phibins
    return np.radians(incr*binn)

def bin2phideg(binn):
    incr = float(360)/phibins
    return incr*binn

def huepeak(img):
    img = img[:,:,0]
    img_flat = img.flatten()
    
    n = len(img_flat)
    thetahat = np.std(img_flat)
    h = 1.06 * thetahat * n**(-1/float(5)) # float() or else python uses int division
    if h==0: # some are zero bc std of hue is zero
        h = 1E-6 # h != 0 so kde will work

    X = img_flat[:, np.newaxis]
    X_plot = np.linspace(0,1,phibins_all)[:, np.newaxis] # phibins_all > phibins; smoothing factor
            
    kde = KernelDensity(kernel='gaussian', bandwidth=h).fit(X)
    log_dens = kde.score_samples(X_plot)
    return np.argmax(log_dens) 

def extract(local_path):
    """Extracts hue,sat,huepeak. Note that during
    slice_crop_extract.py, any with <3 channels were 
    discarded. So these are all 3-channel slices. And 
    since val was already extracted, we are just adding
    to that."""

    img = color.rgb2hsv(imread(local_path))
    hue = np.mean(img[:,:,0])
    sat = np.mean(img[:,:,1])
    peak = huepeak(img)

    return hue,sat,peak

for i in range(len(city_table))[:76]: # not all cities ready yet
    city = city_table.Center.iloc[i]
    CITYDIR = DIR + city + "/"
    yrs = [2012,2014]
    for yr in yrs:
        city_file = CITYDIR + str(yr) + ".csv"
        df = pd.read_csv(city_file)

        """Extract hue, saturation and huepeak."""
        r_all = int(math.ceil(np.sqrt(len(df)/np.pi)))
        phibins_all = int(math.ceil( len(df) / r_all ))
        props = df.local_path.apply(extract) #Series of tuples
        
        df['hue'] = [item[0] for item in props]
        df['sat'] = [item[1] for item in props]
        df['huepeak'] = [item[2] for item in props]

        """Save df. Note that the path is diff than in 
        image-slices. There, I store the actual slices, 
        and the md files are just <year>.csv within the
        relevant folders. Here, all md files in one folder."""
        df.to_csv(SAVEDIR+city+"_"+str(yr)+".csv",index=False)

        tmp = df[df.hue>0]
        tmp = tmp[tmp.sat>0.66]
        tmp = tmp[tmp.val>0.66] #val already in data

        """Radius and bins."""
        r = int(math.ceil(np.sqrt(len(tmp)/np.pi)))
        phibins = int(math.ceil( len(tmp) / r ))
        
        """Creating plotting coordinate columns."""
        tmp.sort_values(by="huepeak",inplace=True)
        binlabels = np.repeat(range(phibins),r)
        
        if len(tmp) > len(binlabels): # it shouldn't be
            tmp = tmp.iloc[:len(binlabels),:]
        elif len(tmp) < len(binlabels):
            binlabels = binlabels[:len(tmp)]

        tmp['xbin'] = binlabels

        px_w = (r * 2 * thumb_side) + thumb_side
        px_h = px_w
        
        canvas = Image.new('RGB',(px_w,px_h),(100,100,100))
        
        bins = list(set(list(tmp.xbin)))
        bins.sort()

        for item in bins:
            
            temp = tmp[tmp.xbin==item]
            temp.sort_values(by="sat",ascending=True,inplace=True) # most sat in center
            temp.reset_index(drop=True,inplace=True)

            for j in range(len(temp)):
                im = Image.open(temp.local_path.loc[j])
                im = im.convert('RGBA')
                im.thumbnail((thumb_side,thumb_side),Image.ANTIALIAS)
                pos = r - j
                xy = pol2cart(pos,bin2phi(item))
                phi = bin2phideg(item)
                im = im.rotate(phi,expand=1)
                
                xcoord = int(round((xy[0] + r) * thumb_side))
                ycoord = int(round((r - xy[1]) * thumb_side)) #bc high in the image is low y
                canvas.paste(im,(xcoord,ycoord),im) # tmp treated as a mask for itself
                    
            print(city,yr,item,"of",len(bins))
                
        attr_str = str(yr)+"_"+str(len(tmp))
        canvas.save(TARGET+city+"_"+attr_str+".png") 
        
        
        
        
        