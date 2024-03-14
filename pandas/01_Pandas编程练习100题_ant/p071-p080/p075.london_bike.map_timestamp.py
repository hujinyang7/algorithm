import pandas as pd

df = pd.read_csv("london_bike.csv")

print(df.columns)

# 从这里开始完成题目

print(df.info())

df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df.info())
