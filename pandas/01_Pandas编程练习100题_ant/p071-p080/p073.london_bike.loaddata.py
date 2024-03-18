# 伦敦共享单车数据集加载CSV数据集查看信息
import pandas as pd

df = pd.read_csv("london_bike.csv")

print(df.head(5))
print(df.info())
