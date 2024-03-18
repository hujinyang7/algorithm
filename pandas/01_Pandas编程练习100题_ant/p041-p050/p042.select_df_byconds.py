# 使用多个条件复杂筛选DataFrame
import numpy as np
import pandas as pd

np.random.seed(66)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']

# 从这里开始完成题目

print(df[(df["col2"] >= 0) & (df["col2"] <= 1)])

