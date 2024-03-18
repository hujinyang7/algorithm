# 伦敦共享单车数据集查询周末数据并实现复制
import pandas as pd

df = pd.read_csv("london_bike.csv")

# 从这里开始完成题目
print(df.columns)

df_new = df.query("is_weekend == 1").copy()
print(df_new)

