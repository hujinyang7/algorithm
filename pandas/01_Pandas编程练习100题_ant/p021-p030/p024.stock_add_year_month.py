# 给数据添加月份和年份

import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df)

# 从这里开始完成题目

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

print(df)
