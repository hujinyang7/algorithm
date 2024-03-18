# 保险费用数据集加载并查看数据信息
import pandas as pd

df = pd.read_csv("insurance.csv")

print(df.head(5))
