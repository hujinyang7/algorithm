# 将DF前几行转换成数据字典
import numpy as np
import pandas as pd

np.random.seed(66)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']

# 从这里开始完成题目
print(df.head(5))
print(df.head(5).to_dict())

