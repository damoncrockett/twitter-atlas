import pandas as pd 
import glob,os
import numpy as np 
import math

def gethue(huepeak):
    return huepeak / float(phibins_all)

BASEDIR = "/data/damoncrockett/twitter-atlas/"
TABLEDIR = BASEDIR + "image-slices-plus/"
TARGET = BASEDIR + "image-slices-plus-plus/"

tblpaths = glob.glob(os.path.join(TABLEDIR,"*.csv"))

for tblpath in tblpaths:
    basename = os.path.basename(tblpath)
    
    df = pd.read_csv(tblpath)
    df.rename(columns={"huepeak":"huepeak_bin"},inplace=True)

    r_all = int(math.ceil(np.sqrt(len(df)/np.pi)))
    phibins_all = int(math.ceil( len(df) / r_all ))
    
    df['huepeak'] = df.huepeak_bin.apply(gethue)

    df.to_csv(TARGET+basename,index=False)


