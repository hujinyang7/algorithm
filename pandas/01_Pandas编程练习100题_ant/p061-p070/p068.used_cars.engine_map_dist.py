# 二手汽车数据集排量字段的处理与分布
import pandas as pd

df = pd.read_csv("used_cars.csv", index_col=0)
df.columns = [col.lower() for col in df.columns]
df.dropna(inplace=True)
print(df[["name", "engine"]].head(5))
# 从这里开始完成题目

df["engine"] = df["engine"].map(lambda x: int(x[:-3]))

print(df["engine"].value_counts())
print(df[["name", "engine"]].head(5))

