BASE = "/data/damoncrockett/twitter-atlas/"
DIR = BASE + "city-tables-wide-combined-10km-bracketless/"
TARGET = BASE + "images/"

import pandas as pd
import glob
import os
import requests
import shutil

all_files = glob.glob(os.path.join(DIR,"*.csv"))

file_counter=0
for file in all_files:
    file_counter+=1
    city = os.path.basename(file).split(".")[0]
    
    try:
        os.mkdir(TARGET+city)
    except:
        pass
    
    tmp = pd.read_csv(file)
    
    for i in range(len(tmp)):
        path = TARGET+city+"/" + os.path.basename(tmp.media_url.loc[i])
        
        try:
            r = requests.get(tmp.media_url.loc[i],stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            print file_counter,city,i,"of",len(tmp)
        
        except Exception as e:
            print e