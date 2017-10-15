import pandas as pd 
import numpy as np
import glob,os 

BASEDIR = "/data/damoncrockett/twitter-atlas/"
MD12 = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
MD14 = BASEDIR + "image-slices-plus-plus-timestamp/"

# 2012 table

tables = glob.glob(os.path.join(MD12,"*.csv"))
basenames = [os.path.basename(item) for item in tables]
cities = [item.split("_")[0] for item in basenames]

df = pd.DataFrame({"city":cities})

# create vector lists for each channel
vals = []
sats = []
hues = []

for i in range(len(tables)):
    table = tables[i]
    city = cities[i]

    tmp = pd.read_csv(table)

    # val
    tmp['valbin'] = pd.cut(tmp.val,10,labels=False)
    vals.append(tmp.valbin.value_counts(normalize="boolean").sort_index())
    
    # sat
    tmp['satbin'] = pd.cut(tmp.sat,10,labels=False)
    sats.append(tmp.satbin.value_counts(normalize="boolean").sort_index())

    # hue
    tmp['polarhue'] = [item * 360 for item in tmp.huepeak]

    # color groups derived phenomenologically; names are conventional
    cnames = []
    for j in range(len(tmp)):
        hue = tmp.polarhue.iloc[j]
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
    tmp['color'] = cnames

    hues.append(tmp.color.value_counts(normalize="boolean").sort_index())

    print("2012",i,city)

df['val'] = vals
df['sat'] = sats
df['hue'] = hues

df.to_csv(BASEDIR+"image-data-histograms_2012.csv")