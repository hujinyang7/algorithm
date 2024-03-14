

import pandas as pd

df = pd.read_csv("./00700.HK.csv", index_col=0)

print(df.head())
print(df.columns)

df.reset_index(inplace=True)
print(df.head())
print(df.columns)
