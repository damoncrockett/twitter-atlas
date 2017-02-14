import glob
import os
import pandas as pd
DIR = "/data/damoncrockett/2014/"

cols = [
"mongo_id",
"lon",
"lat",
"media_url",
"postedTime"
]

counter = -1
for file in glob.glob(os.path.join(DIR,"*.csv")):
    counter+=1
    tmp = pd.read_csv(file)
    tmp = tmp[cols]

    if counter==0:
        d = tmp
    else:
        d = d.append(tmp)

d.to_csv("/data/damoncrockett/twitter_metadata_2014_mezzo.csv",index=False)
