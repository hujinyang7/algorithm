# 伦敦共享单车数据集周末每小时分享次数统计
import pandas as pd

df = pd.read_csv("london_bike.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['month'] = df['timestamp'].dt.month

# 从这里开始完成题目

df_agg = df.groupby(["is_weekend", "hour"])["cnt"].mean().reset_index()
print(df_agg)
