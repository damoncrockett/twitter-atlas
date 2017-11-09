import glob,os
import pandas as pd
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
DIR12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
DIR14 = BASEDIR + "image-slices-plus-plus-timestamp/"

tables12 = glob.glob(os.path.join(DIR12,"*.csv"))

tables14 = glob.glob(os.path.join(DIR14,"*.csv"))
tables14 = [item for item in tables14 if '2014' in item] # bc there are 2012 files in there too

tmphue = []
for table in tables12:
    print("2012",tables12.index(table))
    tmp = pd.read_csv(table)
    tmphue.append(tmp.huepeak)

tmphue = [item for sublist in tmphue for item in sublist]
tmphue = [item * 360 for item in tmphue]
cnames = []
for hue in tmphue:
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
huepdist = list(cnames.hue.value_counts(normalize="boolean").sort_index())

df = pd.DataFrame({"hue":["red","orange","yellow","green","cyan","blue","purple","magenta"],
                   "twelve":huepdist})

tmphue = []
for table in tables14:
    print("2014",tables14.index(table))
    tmp = pd.read_csv(table)
    tmphue.append(tmp.huepeak)

tmphue = [item for sublist in tmphue for item in sublist]
tmphue = [item * 360 for item in tmphue]
cnames = []
for hue in tmphue:
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
huepdist = list(cnames.hue.value_counts(normalize="boolean").sort_index())

df['fourteen'] = huepdist

df.to_csv(BASEDIR+"slice-agg-stats-hue.csv",index=False)