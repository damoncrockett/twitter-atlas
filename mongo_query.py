from pymongo import MongoClient
import pandas as pd
import numpy as np

client = MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

DIR = "/data/damoncrockett/Topic_Atlas/"

query = {}
projection = {'_id' : 1, 'body' : 1}

n = coll.find(query,projection).count()

breaks = list(np.arange(0,n,1000000))
breaks.append(n)
m = len(breaks)

counter = -1
for i in range(m-1):
    cur = coll.find(query,projection)[breaks[i]:breaks[i+1]]
    
    metadata = [m for m in cur]
    mongo_id = [item['_id'] for item in metadata]
    
    text = [item['body'] for item in metadata]
    text = [item.encode('utf-8') if isinstance(item,unicode) else item for item in text]
    
    df = pd.DataFrame(mongo_id,columns=['mongo_id'])
    df['text'] = text
    
    counter+=1
    df.to_csv(DIR + "messages_chunk_" + str(counter) + ".csv", index=False)
    
    print counter
    

