import glob,os
import pandas as pd

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

tmpval = []
tmpsat = []
for table in tables12:
    print("2012",tables12.index(table))
    tmp = pd.read_csv(table)
    tmpval.append(tmp.val)
    tmpsat.append(tmp.sat)

tmpval = [item for sublist in tmpval for item in sublist]
tmpsat = [item for sublist in tmpsat for item in sublist]

tmp = pd.DataFrame({"val":tmpval,
                    "sat":tmpsat})
                    
tmp.val = pd.cut(tmp.val,10,labels=False)
tmp.sat = pd.cut(tmp.sat,10,labels=False)

valpdist = list(tmp.val.value_counts(normalize="boolean").sort_index())
satpdist = list(tmp.sat.value_counts(normalize="boolean").sort_index())

df = pd.DataFrame({"val12":valpdist,
                   "sat12":satpdist})

tmpval = []
tmpsat = []
for table in tables14:
    print("2014",tables14.index(table))
    tmp = pd.read_csv(table)
    tmpval.append(tmp.val)
    tmpsat.append(tmp.sat)

tmpval = [item for sublist in tmpval for item in sublist]
tmpsat = [item for sublist in tmpsat for item in sublist]

tmp = pd.DataFrame({"val":tmpval,
                    "sat":tmpsat})
                    
tmp.val = pd.cut(tmp.val,10,labels=False)
tmp.sat = pd.cut(tmp.sat,10,labels=False)

valpdist = list(tmp.val.value_counts(normalize="boolean").sort_index())
satpdist = list(tmp.sat.value_counts(normalize="boolean").sort_index())

df['val14'] = valpdist
df['sat14'] = satpdist

df.to_csv(BASEDIR+"slice-agg-stats-bins.csv",index=False)