# 保险费用数据集检测是否有重复数据行
import pandas as pd

df = pd.read_csv("insurance.csv")

# 从这里开始完成题目
print(df.head())
print(df.duplicated())
print()
print(df[df.duplicated()])
