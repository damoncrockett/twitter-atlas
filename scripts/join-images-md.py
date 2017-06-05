import pandas as pd 
import glob,os

BASEDIR = "/data/damoncrockett/twitter-atlas/"
SLICEDIR = BASEDIR + "image-slices-plus-plus/"
MDDIR = BASEDIR + "images-md/"
TARGET = BASEDIR + "image-slices-plus-plus-timestamp/"

slicetables = glob.glob(os.path.join(SLICEDIR,"*.csv"))

for slicetable in slicetables:
	df = pd.read_csv(slicetable)
	basename = os.path.basename(slicetable)
	city = basename.split(".")[0].split("_")[0]
	print(basename)

	mdtable = MDDIR + city + ".csv"
	d = pd.read_csv(mdtable)
	d = d[['postedTime']]
	d.reset_index(inplace=True)
	d.rename(columns={"index":"idx"},inplace=True)
	d.set_index("idx",inplace=True)

	df = df.join(d,on="idx")

	df.to_csv(TARGET+basename, index=False)