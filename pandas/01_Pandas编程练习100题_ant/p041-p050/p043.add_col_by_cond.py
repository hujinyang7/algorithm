# 根据现有列新增一个新的数据列
import numpy as np
import pandas as pd

np.random.seed(66)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']

# 从这里开始完成题目

df["col3"] = df["col2"].map(lambda x: 1 if x>=0 else -1)
print(df)

