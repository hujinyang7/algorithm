import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)

print(df.columns)

# 从这里开始完成题目

df.drop("New_Price", axis=1, inplace=True)
print(df.columns)

