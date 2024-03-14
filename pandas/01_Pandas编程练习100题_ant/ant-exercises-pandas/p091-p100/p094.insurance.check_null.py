import pandas as pd

df = pd.read_csv("insurance.csv")
print(df.head())

# 从这里开始完成题目

print(df.isnull().sum())
