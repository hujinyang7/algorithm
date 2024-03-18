# 伦敦共享单车数据集给数据集添加“小时”列
import pandas as pd

df = pd.read_csv("london_bike.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 从这里开始完成题目

df["hour"] = df['timestamp'].dt.hour
print(df.head(5))

