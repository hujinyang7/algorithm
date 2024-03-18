# 二手汽车数据集将数据处理后存入csv
import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)
df.columns = [col.lower() for col in df.columns]

# 从这里开始完成题目

df.to_csv("cars.csv", index=False)

