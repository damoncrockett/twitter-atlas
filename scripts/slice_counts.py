import glob,os
import pandas as pd

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

cities = [os.path.basename(item).split("_")[0] for item in tables12]
df12 = pd.DataFrame({"city":cities})
df12['year'] = 2012

nslices = []
for table in tables12:    
    print('2012',tables12.index(table))
    tmp = pd.read_csv(table)
    nslices.append(len(tmp))

df12['nslices'] = nslices

cities = [os.path.basename(item).split("_")[0] for item in tables14]
df14 = pd.DataFrame({"city":cities})
df14['year'] = 2014

nslices = []
for table in tables14:    
    print('2014',tables14.index(table))
    tmp = pd.read_csv(table)
    nslices.append(len(tmp))

df14['nslices'] = nslices

df = df12.append(df14)

df.to_csv(BASEDIR+"image-slices-counts.csv",index=False)