import pandas as pd

df = pd.read_csv("london_bike.csv")

# 从这里开始完成题目
print(df.columns)

df_new = df.query("is_weekend == 1").copy()
print(df_new)

