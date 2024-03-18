# 二手汽车数据集数据介绍和Pandas加载
import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)

print(df.head(5))

