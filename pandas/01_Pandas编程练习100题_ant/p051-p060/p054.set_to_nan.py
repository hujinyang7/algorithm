# 指定单元格设置DataFrame的值
import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
print(df)

# 从这里开始完成题目

df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan

print(df)
