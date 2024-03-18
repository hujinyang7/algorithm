# 保险费用数据集筛选出数字类型的列名
import pandas as pd

df = pd.read_csv("insurance.csv")
print(df.head())

# 从这里开始完成题目

columns = list(df.select_dtypes(include=["float", "int"]).columns)
print(columns)
