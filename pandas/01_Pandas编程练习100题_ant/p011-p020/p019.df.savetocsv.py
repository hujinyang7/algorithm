# df前N行存入CSV文件
import pandas as pd
import numpy as np

df = pd.DataFrame(
	data={
		"norm": np.random.normal(loc=0, scale=1, size=365),
		"uniform": np.random.uniform(low=0, high=1, size=365),
		"binomial": np.random.binomial(n=1, p=0.2, size=365)},
	index=pd.date_range(start='2024-03-15', periods=365))

# 从这里开始完成题目
df.to_csv("分布数据前50.csv")
