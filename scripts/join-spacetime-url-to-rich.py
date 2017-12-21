import pandas as pd
import glob,os 

DIR = "/data/damoncrockett/"
PROJ = DIR + "twitter-atlas/"
TWEETS = PROJ + "tweets/"
RICH = TWEETS + "rich/"
FULL = TWEETS + "full/"

# 2011: add geo to 'rich'

geofile = DIR + "twitter_metadata_2011.csv"
dfgeo = pd.read_csv(geofile)
dfgeo = dfgeo[['mongo_id','lat','lon']]
dfgeo.set_index("mongo_id",inplace=True)

richfile = RICH + "twitter_metadata_2011_rich.csv"
dfrich = pd.read_csv(richfile)
dfrich = dfrich.join(dfgeo,on='mongo_id')

dfrich.to_csv(FULL + "twitter_metadata_2011_full.csv")
print('2011')

# 2012: add geo, time, url to 'rich'

corefile = DIR + "twitter_metadata_2012.csv"
dfcore = pd.read_csv(corefile)
dfcore = dfcore[['mongo_id','lat','lon','postedTime','media_url']]
dfcore.set_index("mongo_id",inplace=True)

richfile = RICH + "twitter_metadata_2012_rich.csv"
dfrich = pd.read_csv(richfile)
dfrich = dfrich.join(dfcore,on='mongo_id')

dfrich.to_csv(FULL + "twitter_metadata_2012_full.csv")
print('2012')

# 2013: add geo, time, url, chunkwise

corefile = DIR + "twitter_metadata_2013.csv"
dfcore = pd.read_csv(corefile)
dfcore = dfcore[['mongo_id','lat','lon','postedTime','media_url']]
dfcore.set_index("mongo_id",inplace=True)

richfiles = glob.glob(os.path.join(RICH,"*.csv"))
richfiles = [item for item in richfiles if '2013' in item]

counter=-1
for richfile in richfiles:
    counter+=1
    dfrich = pd.read_csv(richfile)
    dfrich = dfrich.join(dfcore,on='mongo_id')
    dfrich.to_csv(FULL + "twitter_metadata_2013_full_" + str(counter) + ".csv")
    print(2013,counter,len(richfiles))


# 2014: add geo, time, url, chunkwise

corefile = DIR + "twitter_metadata_2014_mezzo.csv"
dfcore = pd.read_csv(corefile)
dfcore = dfcore[['mongo_id','lat','lon','postedTime','media_url']]
dfcore.set_index("mongo_id",inplace=True)

richfiles = glob.glob(os.path.join(RICH,"*.csv"))
richfiles = [item for item in richfiles if '2014' in item]

counter=-1
for richfile in richfiles:
    counter+=1
    dfrich = pd.read_csv(richfile)
    dfrich = dfrich.join(dfcore,on='mongo_id')
    dfrich.to_csv(FULL + "twitter_metadata_2014_full_" + str(counter) + ".csv")
    print(2014,counter,len(richfiles))