import pandas as pd 
import glob,os

PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TABLEDIR = DIR + "500-city-tables-10km/" 
ACTORDIR = DIR + "actor-tables/"
TARGET = DIR + "500-city-tables-10km-wide/"

tables = [
          "Hyderabad_2011.csv",
          "Hyderabad_2012.csv",
          "Hyderabad_2013.csv",
          "Hyderabad_.csv",
          "Valencia_2011.csv",
          "Valencia_2012.csv",
          "Valencia_2013.csv",
          "Valencia_.csv"
         ]

years = ['2011','2012','2013','']

counter=-1
for year in years:
    tmp = [item for item in tables if os.path.basename(item).split("_")[1][:-4]==year]
    
    # hack bc I was stupid
    if year=='':
        year = "2014"
    
    actortable = pd.read_csv(ACTORDIR+year+".csv")
    actortable.set_index("mongo_id",inplace=True)
    
    for table in tmp:
        counter+=1
        basename = os.path.basename(table)
        city = basename.split("_")[0]
        year = basename.split("_")[1][:-4]
        
        df = pd.read_csv(TABLEDIR+table)
        df = df.join(actortable,on="mongo_id")

        print(counter,table)
        df.to_csv(TARGET+city+"_"+year+".csv",index=False)
