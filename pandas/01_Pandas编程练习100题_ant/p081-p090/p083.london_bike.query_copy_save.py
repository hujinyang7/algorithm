import pandas as pd

df = pd.read_csv("london_bike.csv")

# 从这里开始完成题目

df_weekend = df.query("is_weekend == 1").copy()
df_weekend.to_csv("weekend.csv", index=False)

