BASE = "/data/damoncrockett/twitter-atlas/"
IMGMD = BASE+"images-md/"

import pandas as pd
citydf = pd.read_csv(BASE+"city-list-count-10km.csv")

total = []
actors = []
for city in citydf.Center:
    srcpath = IMGMD+city+".csv"
    df = pd.read_csv(srcpath)
    total.append(len(df))
    actors.append(len(df.actor_id.unique()))

citydf["total_img"] = total
citydf["actors"] = actors
citydf.to_csv(BASE+"city-list-count-10km-img.csv",index=False)