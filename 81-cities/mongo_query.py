import pymongo
import pandas as pd
import sys
import numpy as np

yr = sys.argv[1]

client = pymongo.MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

DIR = "/data/damoncrockett/twitter-atlas/tweets/"

query = {
'twitter_entities.hashtags':{'$exists':1},
'actor.id':{'$exists':1}
}

projection = {
'_id' : 1, 
'body' : 1,
'twitter_entities.hashtags' : 1,
'actor.id': 1
}

cur = coll.find(query,projection)
num_tweets = cur.count()
chunk_size = 10000000
chunk_edges = np.arange(0,num_tweets,chunk_size)
chunk_edges = np.append(chunk_edges,num_tweets)

for i in range(len(chunk_edges)-1):
	print i,"out of",len(chunk_edges)-1
	cur = coll.find(query,projection)[chunk_edges[i]:chunk_edges[i+1]]
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

	print "building actor_id list..."
	actor_id = [item['actor']['id'].split(":")[2] for item in metadata]

	print "making dataframe..."
	df = pd.DataFrame()
	print "adding columns..."
	df['mongo_id'] = mongo_id
	df['actor_id'] = actor_id
	df['text'] = text
	df['hashtags'] = hashtags

	print "saving csv..."
	
	df.to_csv(DIR+"twitter_metadata_"+str(yr)+"_rich_"+str(i)+".csv",
	encoding="utf-8",
	index=False)