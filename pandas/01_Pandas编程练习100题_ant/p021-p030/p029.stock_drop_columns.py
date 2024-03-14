import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))

# 从这里开始完成题目
df.drop(columns=["High", "Low"], inplace=True)
print(df.head(3))
