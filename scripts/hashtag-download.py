import pandas as pd 
import glob,os

DIR = "/data/damoncrockett/twitter-atlas/"
HASH = DIR + "hashtags/"

hashtables = glob.glob(os.path.join(DIR,"*.csv"))

counter=-1
for hashtable in hashtables:
	counter+=1
	basename = os.path.basename(hashtable)
	foldername = basename[:-4]
	TARGET = HASH + foldername + "/"

	