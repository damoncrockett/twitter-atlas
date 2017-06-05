import pandas as pd
import numpy as np

BASEDIR = "/data/damoncrockett/twitter-atlas/"
FOURDIR = BASEDIR + "image-slices-plus-plus-timestamp/"
TWODIR = BASEDIR + "image-slices-plus-plus-timestamp-trunc/"
CITYTABLE = BASEDIR + "city-list-count-10km-img.csv"

city_table = pd.read_csv(CITYTABLE)
city_table.sort_values(by="total_img",inplace=True)

yrs = [2012, 2014]

cities = []
years = []

vten = []
vthirty = []
vfifty = []
vseventy = []
vninety = []

sten = []
sthirty = []
sfifty = []
sseventy = []
sninety = []

hten = []
hthirty = []
hfifty = []
hseventy = []
hninety = []

for i in city_table.index:
    city = city_table.Center.loc[i]

    for yr in yrs:
        print(city,str(yr))

        cities.append(city)
        years.append(yr)

        if yr==2012:
            DDIR = TWODIR
        elif yr==2014:
            DDIR = FOURDIR

        df = pd.read_csv(DDIR + city + "_" + str(yr) + ".csv")

        vten.append(np.percentile(df.val,10))
        vthirty.append(np.percentile(df.val,30))
        vfifty.append(np.percentile(df.val,50))
        vseventy.append(np.percentile(df.val,70))
        vninety.append(np.percentile(df.val,90))

        sten.append(np.percentile(df.sat,10))
        sthirty.append(np.percentile(df.sat,30))
        sfifty.append(np.percentile(df.sat,50))
        sseventy.append(np.percentile(df.sat,70))
        sninety.append(np.percentile(df.sat,90))

        hten.append(np.percentile(df.huepeak,10))
        hthirty.append(np.percentile(df.huepeak,30))
        hfifty.append(np.percentile(df.huepeak,50))
        hseventy.append(np.percentile(df.huepeak,70))
        hninety.append(np.percentile(df.huepeak,90))

tmp = pd.DataFrame({
            "city":cities,
            "year":years,
            "val10":vten,
            "val30":vthirty,
            "val50":vfifty,
            "val70":vseventy,
            "val90":vninety,
            "sat10":sten,
            "sat30":sthirty,
            "sat50":sfifty,
            "sat70":sseventy,
            "sat90":sninety,
            "hue10":hten,
            "hue30":hthirty,
            "hue50":hfifty,
            "hue70":hseventy,
            "hue90":hninety
            })

tmp.to_csv(BASEDIR+"summary_stats.csv",index=False)

    
