import pandas as pd
tweets = pd.read_csv("/data/damoncrockett/2011/output_2011.csv")
DIR = "/data/damoncrockett/Twitter_Global_Viz/ua11/"
df = pd.read_csv("./world_ua_bboxes.csv")

cnt = []

for i in range(len(df)):
    Center = df.Center.loc[i]
    Country = df.Country.loc[i]
    left = df.left.loc[i]
    top = df.top.loc[i]
    right = df.right.loc[i]
    bottom = df.bottom.loc[i]
    
    tmp = tweets[tweets.lon > left]
    tmp = tmp[tmp.lon < right]
    tmp = tmp[tmp.lat > bottom]
    tmp = tmp[tmp.lat < top]
    n = len(tmp)    

    tmp.to_csv(DIR+Center+"_"+Country+".csv",index=False)
    cnt.append(n)
    print i,Center,n

df['tweet_count_2011'] = cnt
df.to_csv("./world_ua_bboxes_tweetcount.csv",index=False)

    
