BASE = "/data/damoncrockett/twitter-atlas/"
SRC = BASE+"city-tables-wide-combined-10km-bracketless/"
IMG = BASE+"images/"
IMGMD = BASE+"images-md/"

import pandas as pd
import glob
import os

citylist = pd.read_csv(BASE+"city-list.csv")
citylist = list(citylist.Center)

counter=0
for city in citylist:
    counter+=1
    
    srcpath = SRC+city+".csv"
    targetpath = IMGMD+city+".csv"
    imgdir = IMG+city+"/"
    imglist = glob.glob(os.path.join(imgdir,"*.jpg"))
    
    df = pd.DataFrame()
    df['local_path'] = imglist
    df['basename'] = df.local_path.apply(os.path.basename)
    
    srcdf = pd.read_csv(srcpath)
    srcdf['basename'] = srcdf.media_url.apply(os.path.basename)
    srcdf.set_index("basename",inplace=True)
    
    df = df.join(srcdf,on="basename")
    df.to_csv(targetpath,index=False)
    print counter,city

    
