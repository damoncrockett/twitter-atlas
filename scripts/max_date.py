import pandas as pd 
from dateutil import parser
import glob,os

DIR = "/data/damoncrockett/twitter-atlas/images-md/"

citytables = glob.glob(os.path.join(DIR,"*.csv"))

maxes = []

for citytable in citytables:
    df = pd.read_csv(citytable)
    df.postedTime = df.postedTime.apply(parser.parse)
    
    city = os.path.basename(citytable).split(".")[0]
    tablemax = max(df.postedTime)
    print(city,tablemax)
    maxes.append(tablemax)

print(max(maxes))