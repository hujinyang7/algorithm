import pandas as pd

df = pd.read_csv("london_bike.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 从这里开始完成题目

df["hour"] = df['timestamp'].dt.hour
print(df.head(5))

