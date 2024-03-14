
import pandas as pd

df = pd.read_csv("分布数据前50.csv", index_col=0)

print(df.info())

print(df.head())
