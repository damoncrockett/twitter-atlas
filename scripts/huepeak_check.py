BASEDIR = "/data/damoncrockett/twitter-atlas/"
SLICEDATADIR = BASEDIR + "image-slices-plus-plus/"
TARGET = BASEDIR + "huepeak-check/"

import pandas as pd 
import glob,os
from PIL import Image
import numpy as np

tblpaths = glob.glob(os.path.join(SLICEDATADIR,"*.csv"))
hueticks = np.arange(0,1.1,.1)
thumb_side = 16
px_w = ( len(hueticks) - 1 ) * thumb_side
px_h = px_w

for tblpath in tblpaths:
    print(tblpath)
    basename = os.path.basename(tblpath)
    stem = basename.split(".")[0]
    
    df = pd.read_csv(tblpath)
    df['xbin'] = pd.cut(df.huepeak,hueticks,labels=False)
    df.xbin.fillna(0,inplace=True)
    df.xbin = df.xbin.apply(int)


    canvas = Image.new('RGB',(px_w,px_h),'hsl(0,0%,50%)')

    for bin in df.xbin.unique():
        tmp = df[df.xbin==bin]
        tmp = tmp.iloc[:10]
        xcoord = bin * thumb_side
        ycoord = px_h - thumb_side

        for i in tmp.index:
            im = Image.open(tmp.local_path.loc[i])
            canvas.paste(im,(xcoord,ycoord))
            ycoord = ycoord - thumb_side

    canvas.save(TARGET+basename+".png")
    






    

