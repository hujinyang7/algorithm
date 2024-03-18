# 移除DataFrame中数据值为空的行
import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
print(df)

# 从这里开始完成题目

df2 = df.dropna()
print(df2)

