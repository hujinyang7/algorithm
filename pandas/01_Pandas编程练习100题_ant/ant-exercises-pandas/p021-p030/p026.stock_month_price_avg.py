import pandas as pd

df = pd.read_csv("./00700.HK.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
print(df)

# 从这里开始完成题目

print(df.groupby("Year")["Close"].mean())


