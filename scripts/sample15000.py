import pandas as pd
from dateutil import parser

DIR = "/data/damoncrockett/twitter-atlas/"
SMP = DIR + "sample-for-tagging/derived/"
MD = DIR + "images-md/"

smptable = pd.read_csv(SMP+"sample_all.csv")
smpidxs = smptable.mongo_id

cities = ['Manila','Mexico City','Moscow','Paris','Tokyo']

counter = -1
for city in cities:
    counter+=1
    print(city)
    meta = pd.read_csv(MD+city+".csv")
    meta = meta[-meta.mongo_id.isin(smpidxs)] # notice the negation
    meta.postedTime = meta.postedTime.apply(parser.parse)
    meta['month'] = [item.month for item in meta.postedTime]
    meta['year'] = [item.year for item in meta.postedTime]
    meta['city'] = city

    t12 = meta[meta.year==2012]
    t12 = t12[t12.month==5]
    
    try:
        t12 = t12.sample(n=1500)
    except:
        print('2012',city,len(t12))

    t14 = meta[meta.year==2014]
    t14 = t14[t14.month==5]
    
    try:
        t14 = t14.sample(n=1500)
    except:
        print('2014',city,len(t14))

    tmp = t12.append(t14)

    if counter==0:
        df = tmp
    else:
        df = df.append(tmp)

df.to_csv(SMP+"sample_all_secondpass.csv",index=False)

if len(set(smpidxs).intersection(set(df.mongo_id)))==0:
    print("all unique")