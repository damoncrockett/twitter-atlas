import pandas as pd

DIR = "/data/damoncrockett/"
TARGET = DIR + "twitter-atlas/"
filestring = "twitter_metadata_"

yrs = ["2011","2012","2013","2014_mezzo"]

for yr in yrs:
    filename = filestring+yr+".csv"
    df = pd.read_csv(DIR+filename)
    df = df[['postedTime','lat','lon']]
    df.to_csv(TARGET+filename,index=False)