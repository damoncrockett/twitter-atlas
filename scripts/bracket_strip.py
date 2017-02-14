BASE="/data/damoncrockett/twitter-atlas/" 
DIR=BASE+"city-tables-wide-combined-10km/"
TARGET=BASE+"city-tables-wide-combined-10km-bracketless/"

import glob
import os
import pandas as pd

def bracket_strip(hashtag_string):
    return hashtag_string.translate(None," ").lstrip("[").rstrip("]")

all_files = glob.glob(os.path.join(DIR,"*.csv"))

counter=0
for file in all_files:
    counter+=1
    city = os.path.basename(file).split(".")[0]
    tmp = pd.read_csv(file)
    tmp.hashtags = tmp.hashtags.apply(bracket_strip)
    tmp.to_csv(TARGET+city+".csv",index=False)
    print counter