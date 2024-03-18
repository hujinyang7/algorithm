# 按列名筛选DF使用.loc方法进行
import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10, 4), columns=list("ABCD"))
print(df)

print(df.loc[df['C'] > 0.8])

