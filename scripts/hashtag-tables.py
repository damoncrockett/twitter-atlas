import pandas as pd
import glob,os

DIR = "/data/damoncrockett/twitter-atlas/"
HASH = DIR + "hashtags/"
TWEETS = DIR + "tweets/"

hashtable = pd.read_csv(HASH+"hashtags_counts_top1000.csv")
tweettables = glob.glob(os.path.join(TWEETS,"*.csv"))

def hashparse(item):
    item = item.lstrip("[").rstrip("]")
    l = item.split(",")
    l = [item.lstrip(" ").rstrip(" ") for item in l]
    return l
    
counter = -1    
for hashtag in hashtable.hashtag:
    counter+=1
    
    try:
        os.mkdir(HASH+hashtag+"/")
    except:
        pass

    tcounter = -1
    for tweettable in tweettables:
        tcounter+=1
        basename = os.path.basename(tweettable)
        df = pd.read_csv(tweettable)
        df.hashtags = df.hashtags.apply(hashparse)
        
        taginlist = []
        for i in df.index:
            hashtaglist = df.hashtags.loc[i]
            if hashtag in hashtaglist:
                taginlist.append('yes')
            else:
                taginlist.append('no')
            print(counter,hashtag,tcounter,basename,i)

        df['taginlist'] = taginlist
        df = df[df.taginlist=='yes']

        if tcounter==0:
            tmp = df
        else:
            tmp = tmp.append(df)
    
    del tmp['taginlist']
    tmp.to_csv(HASH+hashtag+".csv",index=False)