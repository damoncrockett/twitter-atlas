import pandas as pd 
from dateutil import parser
import glob,os
import pytz,datetime

BASEDIR = "/data/damoncrockett/twitter-atlas/"
SLICEDIR = BASEDIR + "image-slices-plus-plus-timestamp/"
TARGET = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"

slicetables = glob.glob(os.path.join(SLICEDIR,"*.csv"))
max_date = datetime.datetime(2012,7,14,15,57,0,tzinfo=pytz.utc)

counter=0
for slicetable in slicetables:
    counter+=1
    basename = os.path.basename(slicetable)
    year = basename.split(".")[0].split("_")[1]
    if year=="2012":
        df = pd.read_csv(slicetable)
        df.postedTime = df.postedTime.apply(parser.parse)
        df_trunc = df[df.postedTime <= max_date]
        df_trunc.to_csv(TARGET+basename,index=False)
        print(counter,basename,len(df),len(df_trunc))


