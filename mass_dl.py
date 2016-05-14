import pandas as pd
import os

DIR = "/Users/damoncrockett/Desktop/Topic_Atlas_Data/"
infile = DIR + "twitter_2014_sd_all_CPA.csv"
BASE_PATH = DIR + "images/"

df = pd.read_csv(infile)

import requests
import shutil

n = len(df.index)

status_code = []

for i in range(n):
    path = BASE_PATH + os.path.basename(df.media_url.loc[i])
    print i,path

    try:
        r = requests.get(df.media_url.loc[i],stream=True)
        if r.status_code == 200:
            status_code.append("two_hundo")
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)  
    except:
        status_code.append("bad_link")
        print "bad_link"
        
df['status_code'] = status_code
df.to_csv(infile,index=False)