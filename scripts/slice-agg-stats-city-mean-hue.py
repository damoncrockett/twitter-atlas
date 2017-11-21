import glob,os
import pandas as pd
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
META = BASEDIR + "image-slices-counts-std.csv"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

master = pd.read_csv(META)
master['meanval'] = 0
master['meansat'] = 0
master['huevec'] = ''

for table in tables12:    
    print('2012',tables12.index(table))
    city = os.path.basename(table).split("_")[0]
    idx = master.index[(master.city==city)&(master.year==2012)][0]

    tmp = pd.read_csv(table)

    meanval = np.mean(tmp.val)
    meansat = np.mean(tmp.sat)
    hues = [item * 360 for item in tmp.huepeak]

    cnames = []
    for hue in hues:
        if hue < 20:
            cnames.append("1red")
        elif 20 <= hue < 50:
            cnames.append("2orange")
        elif 50 <= hue < 70:
            cnames.append("3yellow")
        elif 70 <= hue < 160:
            cnames.append("4green")
        elif 160 <= hue < 200:
            cnames.append("5cyan")
        elif 200 <= hue < 260:
            cnames.append("6blue")
        elif 260 <= hue < 285:
            cnames.append("7purple")
        elif 285 <= hue < 330:
            cnames.append("8magenta")
        elif hue >= 330:
            cnames.append("1red")

    cnames = pd.DataFrame({"hue":cnames})
    huevec = list(cnames.hue.value_counts(normalize="boolean").sort_index())
    huevecstring = '_'.join(str(item) for item in huevec)

    master.meanval.loc[idx] = meanval
    master.meansat.loc[idx] = meansat
    master.huevec.loc[idx] = huevecstring

for table in tables14:    
    print('2014',tables14.index(table))
    city = os.path.basename(table).split("_")[0]
    idx = master.index[(master.city==city)&(master.year==2014)][0]

    tmp = pd.read_csv(table)

    meanval = np.mean(tmp.val)
    meansat = np.mean(tmp.sat)
    hues = [item * 360 for item in tmp.huepeak]

    cnames = []
    for hue in hues:
        if hue < 20:
            cnames.append("1red")
        elif 20 <= hue < 50:
            cnames.append("2orange")
        elif 50 <= hue < 70:
            cnames.append("3yellow")
        elif 70 <= hue < 160:
            cnames.append("4green")
        elif 160 <= hue < 200:
            cnames.append("5cyan")
        elif 200 <= hue < 260:
            cnames.append("6blue")
        elif 260 <= hue < 285:
            cnames.append("7purple")
        elif 285 <= hue < 330:
            cnames.append("8magenta")
        elif hue >= 330:
            cnames.append("1red")

    cnames = pd.DataFrame({"hue":cnames})
    huevec = list(cnames.hue.value_counts(normalize="boolean").sort_index())
    huevecstring = '_'.join(str(item) for item in huevec)

    master.meanval.loc[idx] = meanval
    master.meansat.loc[idx] = meansat
    master.huevec.loc[idx] = huevecstring

master.to_csv(BASEDIR+"image-slices-counts-std-mean-hue.csv",index=False)