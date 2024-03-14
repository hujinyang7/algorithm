import pandas as pd

df = pd.read_csv("./00700.HK.csv")

# 从这里开始完成题目

print(df["Close"].min())
print(df["Close"].argmin())
print(df.loc[[df["Close"].argmin()]])
