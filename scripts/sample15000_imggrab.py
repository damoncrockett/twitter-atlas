import pandas as pd
import os
import shutil

DIR = "/data/damoncrockett/twitter-atlas/"
SMP = DIR + "sample-for-tagging/derived/"

df = pd.read_csv(SMP+"sample_all_secondpass.csv")

try:
    os.mkdir(SMP+"secondpass/")
except:
    pass

TARGET = SMP + "secondpass/"

for i in df.index:
    local_path = df.local_path.loc[i]
    shutil.copy(local_path,TARGET)