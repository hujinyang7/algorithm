# 合并两个Series生成一个DataFrame
import numpy as np
import pandas as pd

np.random.seed(66)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ["col1", "col2"]
print(df)
