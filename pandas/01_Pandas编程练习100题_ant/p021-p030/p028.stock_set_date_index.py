import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))

# 从这里开始完成题目
df.set_index("Date", inplace=True)
print(df.head(3))
