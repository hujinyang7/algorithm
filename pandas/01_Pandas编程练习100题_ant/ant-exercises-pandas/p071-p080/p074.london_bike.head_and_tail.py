import pandas as pd

df = pd.read_csv("london_bike.csv", index_col=0)

# 从这里开始完成题目

print(df.head(5))
print(df.tail(5))
