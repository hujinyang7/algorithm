import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)
df.columns = [col.lower() for col in df.columns]

# 从这里开始完成题目

print(df.columns)
print(df["transmission"].value_counts())
df["transmission"] = df["transmission"].map({"Manual":0, "Automatic":1})
print(df["transmission"].value_counts())

