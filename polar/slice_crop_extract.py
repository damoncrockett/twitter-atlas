import numpy as np
from dateutil import parser
import pandas as pd
import datetime
import pytz
import image_slicer
import os
import glob
from PIL import Image
from skimage.io import imread
from skimage import color
import time as time_module


BASEDIR = "/data/damoncrockett/twitter-atlas/"
CITYDIR = BASEDIR + "images-md/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"
TARGET = BASEDIR + "image-slices/"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

SLICE_RATIO = 240000 / float(512)

for i in city_table.index:

    city = city_table.Center.loc[i]
    df_filestring = CITYDIR + city + ".csv"
    df = pd.read_csv(df_filestring)
    
    df.postedTime = df.postedTime.apply(parser.parse)
    df['isoweekday'] = [item.isoweekday() for item in df.postedTime]
    df['time'] = [item.time() for item in df.postedTime]
    zero = datetime.datetime.combine(datetime.date.today(),datetime.time(0,0,0,0))
    secperday = 86400
    
    secpast = []
    for w in df.index:
    
        isoweekday = df.isoweekday.loc[w]
        time = df.time.loc[w]
        dtime = datetime.datetime.combine(datetime.date.today(),time)
    
        if isoweekday==7:
            secpast.append(int((dtime-zero).total_seconds()))
        else:
            secpast.append(int((dtime-zero).total_seconds()) + (secperday * isoweekday))
        print(i,"secpast",w,"of",len(df))
    
    df['secpast'] = secpast    
    
    df['year'] = [item.year for item in df.postedTime]
    yrs = [2012,2014]
    
    for yr in yrs:
        try:
            os.mkdir(TARGET+city+"/")
        except:
            pass
        try:
            os.mkdir(TARGET+city+"/"+str(yr)+"/")
        except:
            pass
        
        SLICEDIR = TARGET+city+"/"+str(yr)+"/"
        tmp = df[df.year==yr]
        
        imarea = []
        for j in tmp.index:
            try:
                im = Image.open(tmp.local_path.loc[j])
                area = im.size[0] * im.size[1]
                imarea.append(area)
            except:
                imarea.append(None)
            print(i,yr,"area",j,"of",len(tmp))
        
        tmp['imarea'] = imarea
        tmp = tmp[tmp.imarea.notnull()]
        tmp['nslice'] = [int(round( item / SLICE_RATIO )) for item in tmp.imarea]
        
        sliceidx = [list(np.repeat(k,tmp.nslice.loc[k])) for k in tmp.index]
        sliceidx = [item for sublist in sliceidx for item in sublist]
        slicenum = [range(tmp.nslice.loc[k]) for k in tmp.index]
        slicenum = [item for sublist in slicenum for item in sublist]
        slicedf = pd.DataFrame({"sliceidx":sliceidx,"slicenum":slicenum})
        
        sample_size = int(round( len(slicedf) * 0.01 ))
        slicedf = slicedf.sample(n=sample_size)
        idxlist = list(slicedf.sliceidx.unique())
        
        tmp = tmp.loc[idxlist,:]
        for u in tmp.index:
            path = tmp.local_path.loc[u]
            slices = list(slicedf.slicenum[slicedf.sliceidx==u])
            nslice = tmp.nslice.loc[u]
    
            try:
                
                tiles = image_slicer.slice(path,nslice,save=False)
                tile_subset = tuple(tiles[v] for v in slices)
                image_slicer.save_tiles(tile_subset,
                                    directory=SLICEDIR,
                                    prefix=str(u))
                                    
            except Exception as e:
                print(e)
            
            print(i,yr,"slice",u,"of",len(tmp))
    
        actslicedf = pd.DataFrame()
        actslice_paths = glob.glob(os.path.join(SLICEDIR,"*.png"))
        actslicedf['local_path'] = [item for item in actslice_paths]
        actslicedf['basename'] = actslicedf.local_path.apply(os.path.basename)
        actslicedf['idx'] = [int(item.split("_")[0]) for item in actslicedf.basename]
        tmp = tmp[['secpast']]
        tmp['idx'] = tmp.index
        tmp.set_index("idx",inplace=True)
        actslicedf = actslicedf.join(tmp,on="idx")
        actslicedf.secpast = actslicedf.secpast.apply(int)
         
        cropped = []
        val = [] 
        for z in actslicedf.index:
            local_path = actslicedf.local_path.loc[z]
            
            try:
                im = Image.open(local_path)
                w = im.width
                h = im.height

                if w > h:
                    im = im.crop((0,0,h,h))
                    im.save(local_path)
                elif h > w:
                    im = im.crop((0,h-w,w,h))
                    im.save(local_path)
                elif h == w:
                    pass
                    
                cropped.append("cropped")

            except Exception as e:
                print(e)
                cropped.append(None)

            try:
                img = imread(local_path)

                if len(img.shape)==3:
                    img = color.rgb2hsv(img)
                    i_val = np.mean(img[:,:,2])
                    val.append(i_val)

                else:
                    val.append(None)

            except Exception as e:
                print(e)
                val.append(None)
                
            print(i,yr,"crop-extract",z,"of",len(actslicedf))

        print(len(actslicedf),len(cropped))
        actslicedf['cropped'] = cropped
        actslicedf['val'] = val
        actslicedf = actslicedf[actslicedf.cropped.notnull()]
        actslicedf = actslicedf[actslicedf.val.notnull()]
        actslicedf.to_csv(TARGET+city+"/"+str(yr)+".csv",index=False)

