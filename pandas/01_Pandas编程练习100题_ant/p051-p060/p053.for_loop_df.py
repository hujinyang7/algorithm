import numpy as np
import pandas as pd

np.random.seed(66)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

# 从这里开始完成题目

for index, row in df.head(5).iterrows():
	print(row)

