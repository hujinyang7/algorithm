# 保险费用数据集删除重复的数据行
import pandas as pd

df = pd.read_csv("insurance.csv")

# 从这里开始完成题目

print(df.shape)
df = df.drop_duplicates()
print(df.shape)

print(df[df.duplicated()])
