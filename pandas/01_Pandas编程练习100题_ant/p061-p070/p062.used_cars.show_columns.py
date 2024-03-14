import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)

print(df)

# 从这里开始完成题目

print(list(df.columns))

