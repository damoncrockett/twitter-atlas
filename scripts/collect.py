import pandas as pd
import glob
import os
import sys
from numpy import repeat as rep

YEAR = sys.argv[1]

DIR = "/data/damoncrockett/Twitter_Global_Viz/"

cols = [
'mongo_id',
'media_url',
'lon',
'lat',
'postedTime',
'Center',
'Country'
]

df_agg = pd.read_csv(DIR+"world_ua_bboxes_tweetcount.csv")
df_agg = df_agg[['Center','Country']]
df_agg.set_index('Center',inplace=True)

counter=-1
for file in glob.glob(os.path.join(DIR+"ua"+str(YEAR)+"/","*.csv")):
    counter+=1
    city = os.path.basename(file)[:-4]
    df = pd.read_csv(file)
    n = len(df)
    df['Center'] = list(rep(city,n))
    df = df.join(df_agg,on='Center')
    df = df[cols]
    
    if counter==0:
        tmp = df
    else:
        tmp = tmp.append(df)
    print counter,city

tmp.to_csv(DIR+"tgv_"+str(YEAR)+".csv",index=False)
    
# actually now I'm thinking it might not make sense to make year aggs
# Maybe city aggs, actually.
    

    
