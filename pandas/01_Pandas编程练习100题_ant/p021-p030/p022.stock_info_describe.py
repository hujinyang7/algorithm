# 查看基本信息和数据统计

import pandas as pd

df = pd.read_csv("./00700.HK.csv")

print(df.info())
print()
print(df.describe())

