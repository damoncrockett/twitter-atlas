import pandas as pd
import glob,os

DIR = "/data/damoncrockett/twitter-atlas/"
HASH = DIR + "hashtags/"
TWEETS = DIR + "tweets/full/"

hashtable = pd.read_csv(HASH+"hashtags_counts_top1000.csv")
tweettables = glob.glob(os.path.join(TWEETS,"*.csv"))

def hashparse(item):
    item = item.lstrip("[").rstrip("]")
    l = item.split(",")
    l = [item.lstrip(" ").rstrip(" ") for item in l]
    l = '_'.join(l) # turns list into underscore-separated string
    l = "_" + l + "_" # this is crucial for the eventual string search
    return l
    
counter = -1    
for hashtag in hashtable.hashtag:
    counter+=1
    hashstring = "_"+hashtag+"_" # why the above is crucial

    try:
        os.mkdir(HASH+hashtag+"/")
    except:
        pass

    tcounter = -1
    for tweettable in tweettables:
        tcounter+=1
        basename = os.path.basename(tweettable)
        df = pd.read_csv(tweettable)
        df = df[df.hashtags!='[]']
        df.hashtags = df.hashtags.apply(hashparse)
        df = df[df.hashtags.str.contains(hashstring)]
        
        if tcounter==0:
            tmp = df
        else:
            tmp = tmp.append(df)

        print(counter,hashtag,tcounter,basename)
    
    tmp.to_csv(HASH+hashtag+".csv",index=False)