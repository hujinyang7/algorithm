# 加载CSV文件到df
import pandas as pd

df = pd.read_csv("分布数据前50.csv", index_col=0)  # 记得恢复索引列

print(df)

print(df.info())

print(df.head())
