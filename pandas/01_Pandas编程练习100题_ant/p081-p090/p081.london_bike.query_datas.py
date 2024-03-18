# 伦敦共享单车数据集按风速和湿度筛选数据
import pandas as pd

df = pd.read_csv("london_bike.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['month'] = df['timestamp'].dt.month

# 从这里开始完成题目

df = df.query("wind_speed < 10 and hum > 90")
print(df[["wind_speed", "hum"]].head(10))
