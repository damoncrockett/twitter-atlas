import pymongo
import pandas as pd
import numpy as np
from bson.objectid import ObjectId

client = pymongo.MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

DIR = "/data/damoncrockett/Topic_Atlas/"

tmp = pd.read_csv(DIR+"twitter_2014_sd_all_CPA_cleaned.csv")
ids = list(tmp.mongo_id)
ids = [ObjectId(item) for item in ids]

query = {'_id': {'$in': ids}}
projection = {'_id' : 1, 'body' : 1}

cur = coll.find(query,projection)

metadata = [m for m in cur]
mongo_id = [item['_id'] for item in metadata]

text = [item['body'] for item in metadata]
text = [item.encode('utf-8') if isinstance(item,unicode) else item for item in text]

df = pd.DataFrame(mongo_id,columns=['mongo_id'])
df['text'] = text

df.to_csv(DIR + "text.csv", index=False)