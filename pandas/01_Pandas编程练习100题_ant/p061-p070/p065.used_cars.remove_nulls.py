# 二手汽车数据集移除所有包含缺失值的行
import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)
print(df.head(5))

# 从这里开始完成题目

print(df.info())
df.dropna(inplace=True)
print(df.info())
