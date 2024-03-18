# 二手汽车数据集马力字段的处理与分布
import pandas as pd
import numpy as np

df = pd.read_csv("used_cars.csv", index_col=0)
df.columns = [col.lower() for col in df.columns]
df.dropna(inplace=True)

# 从这里开始完成题目

df["power"] = np.where(df["power"] == "null bhp", np.nan, df["power"])

print(df["power"].value_counts()[:5])



