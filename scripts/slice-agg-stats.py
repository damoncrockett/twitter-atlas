import glob,os
import pandas as pd
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

df = pd.DataFrame({"feature":['valmean','valmean','satmean','satmean','valstd','valstd','satstd','satstd'],
                   "year":[2012,2014,2012,2014,2012,2014,2012,2014],
                   "value": 0})

tmpval = []
tmpsat = []
for table in tables12:
    print("2012",tables12.index(table))
    tmp = pd.read_csv(table)
    tmpval.append(tmp.val)
    tmpsat.append(tmp.sat)

tmpval = [item for sublist in tmpval for item in sublist]
tmpsat = [item for sublist in tmpsat for item in sublist]

df['value'].loc[0] = np.mean(tmpval)
df['value'].loc[4] = np.std(tmpval)

df['value'].loc[2] = np.mean(tmpsat)
df['value'].loc[6] = np.std(tmpsat)

tmpval = []
tmpsat = []
for table in tables14:
    print("2014",tables14.index(table))
    tmp = pd.read_csv(table)
    tmpval.append(tmp.val)
    tmpsat.append(tmp.sat)

tmpval = [item for sublist in tmpval for item in sublist]
tmpsat = [item for sublist in tmpsat for item in sublist]

df['value'].loc[1] = np.mean(tmpval)
df['value'].loc[5] = np.std(tmpval)

df['value'].loc[3] = np.mean(tmpsat)
df['value'].loc[7] = np.std(tmpsat)

df.to_csv(BASEDIR+"slice-agg-stats.csv",index=False)
