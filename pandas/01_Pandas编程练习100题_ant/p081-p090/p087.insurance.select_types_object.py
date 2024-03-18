# 保险费用数据集筛选打印object类型的列
import pandas as pd

df = pd.read_csv("insurance.csv")
print(df.head())

# 从这里开始完成题目
print(df.select_dtypes(include=["object"]))
