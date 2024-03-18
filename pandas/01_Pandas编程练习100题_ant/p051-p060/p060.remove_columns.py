# 删除DataFrame指定的数据列
import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
print(df)

# 从这里开始完成题目

print(df.drop("D", axis=1))
print(df.drop(["C", "D"], axis=1))
