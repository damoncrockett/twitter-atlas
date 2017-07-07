import pandas as pd 
import glob,os

PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TABLEDIR = DIR + "500-city-tables-10km/" 
ACTORDIR = DIR + "actor-tables/"
TARGET = DIR + "500-city-tables-10km-wide/"

tables = glob.glob(os.path.join(TABLEDIR,"*.csv"))

counter=-1
for table in tables:
    counter+=1
    basename = os.path.basename(table)
    city = basename.split("_")[0]
    year = basename.split("_")[1][:-4]
    
    # a hack bc I was stupid
    if year=='':
        year = "2014"

    df = pd.read_csv(table)
    actortable = pd.read_csv(ACTORDIR+year+".csv")
    actortable.set_index("mongo_id",inplace=True)
    df = df.join(actortable,on="mongo_id")

    print(counter,table)
    df.to_csv(TARGET+city+"_"+year+".csv",index=False)