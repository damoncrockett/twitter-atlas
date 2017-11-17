import glob,os
import pandas as pd
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
META = BASEDIR + "image-slices-counts.csv"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

master = pd.read_csv(META)
master['stdval'] = 0
master['stdsat'] = 0

for table in tables12:    
    print('2012',tables12.index(table))
    city = os.path.basename(table).split("_")[0]
    idx = master.index[(master.city==city)&(master.year==2012)][0]

    tmp = pd.read_csv(table)

    stdval = np.std(tmp.val)
    stdsat = np.std(tmp.sat)

    master.stdval.loc[idx] = stdval
    master.stdsat.loc[idx] = stdsat

for table in tables14:    
    print('2014',tables14.index(table))
    city = os.path.basename(table).split("_")[0]
    idx = master.index[(master.city==city)&(master.year==2014)][0]

    tmp = pd.read_csv(table)

    stdval = np.std(tmp.val)
    stdsat = np.std(tmp.sat)

    master.stdval.loc[idx] = stdval
    master.stdsat.loc[idx] = stdsat

master.to_csv(BASEDIR+"image-slices-counts-std.csv",index=False)