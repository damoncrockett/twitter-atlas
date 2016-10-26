import pymongo
import pandas as pd
import sys

yr = sys.argv[1]

client = pymongo.MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

DIR = "/data/damoncrockett/"

query = {
'twitter_entities.hashtags':{'$exists':1},
'twitter_entities.media.media_url':{'$exists':1},
'actor.id':{'$exists':1}
}

projection = {
'_id' : 1, 
'body' : 1,
'postedTime': 1, 
'twitter_entities.hashtags' : 1,
'twitter_entities.media.media_url': 1,
'actor.id': 1
}

cur = coll.find(query,projection)
print "getting tweets..."
metadata = [m for m in cur]
print "building id list..."
mongo_id = [item['_id'] for item in metadata]
print "building tweet list..."
text = [item['body'] for item in metadata]
print "replacing newlines and carriage returns..."
text = [item.replace("\n"," ") for item in text]
text = [item.replace("\r"," ") for item in text]

print "building hashtag list..."
hashtags = [item['twitter_entities']['hashtags'] for item in metadata]
hashtags = [[item['text'] for item in l] for l in hashtags]

print "building timestamp list..."
postedTime = [item['postedTime'] for item in metadata]
print "building actor_id list..."
actor_id = [item['actor']['id'].split(":")[2] for item in metadata]

import os
print "building media_url list..."
media_url = [item['twitter_entities']['media'][0]['media_url'] for item in metadata]
s = "http://pbs.twimg.com/media/"
media_url = [s+os.path.basename(item) for item in media_url]

print "making dataframe..."
df = pd.DataFrame()
print "adding columns..."
df['mongo_id'] = mongo_id
df['actor_id'] = actor_id
df['postedTime'] = postedTime
df['media_url'] = media_url
df['text'] = text
df['hashtags'] = hashtags

print "saving csv..."
df.to_csv(DIR+"twitter_metadata_"+str(yr)+"_rich.csv",encoding="utf-8",index=False)