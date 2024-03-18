# 伦敦共享单车数据集修改时间戳字段为时间类型
import pandas as pd

df = pd.read_csv("london_bike.csv")

print(df.columns)

# 从这里开始完成题目

print(df.info())

df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df.info())
