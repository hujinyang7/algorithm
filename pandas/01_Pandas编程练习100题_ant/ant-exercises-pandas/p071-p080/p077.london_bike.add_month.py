import pandas as pd

df = pd.read_csv("london_bike.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

# 从这里开始完成题目

df['month'] = df['timestamp'].dt.month
print(df.head(5))

