import pandas as pd
tweets = pd.read_csv("/data/damoncrockett/twitter_metadata_2013.csv")
DIR = "/data/damoncrockett/Twitter_Global_Viz/ua13/"
df = pd.read_csv("./world_ua_bboxes_tweetcount.csv")

count_2013 = []

for i in range(len(df)):
    Center = df.Center.loc[i]
    left = df.left.loc[i]
    top = df.top.loc[i]
    right = df.right.loc[i]
    bottom = df.bottom.loc[i]
    
    tmp = tweets[tweets.lon > left]
    tmp = tmp[tmp.lon < right]
    tmp = tmp[tmp.lat > bottom]
    tmp = tmp[tmp.lat < top]
    n = len(tmp)    

    tmp.to_csv(DIR+Center+".csv",index=False)
    count_2013.append(n)
    print i,Center,n

df['tweet_count_2013'] = count_2013
df.to_csv("./world_ua_bboxes_tweetcount.csv",index=False)

    
