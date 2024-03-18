# 伦敦共享单车数据集查询周末数据并存入csv
import pandas as pd

df = pd.read_csv("london_bike.csv")

# 从这里开始完成题目

df_weekend = df.query("is_weekend == 1").copy()
df_weekend.to_csv("weekend.csv", index=False)

