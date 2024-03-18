# 筛选出部分数据列
import pandas as pd

df = pd.read_csv("./00700.HK.csv")

print(df.head(3))


# 从这里开始完成题目
df_new = df[["Date", "Open", "Close", "Volume"]]
print(df_new.head(3))
