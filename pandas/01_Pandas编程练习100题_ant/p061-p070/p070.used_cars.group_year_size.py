# 二手汽车数据集统计每年份的二手车数量
import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)
df.columns = [col.lower() for col in df.columns]

# 从这里开始完成题目

print(df.columns)

print(df.groupby("year").size())
