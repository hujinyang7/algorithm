# 生成日期和随机分布DataFrame
import pandas as pd
import numpy as np

date_range = pd.date_range(start='2021-01-01', periods=1000)

data = {
	'norm': np.random.normal(loc=0, scale=1, size=1000),
	'uniform': np.random.uniform(low=0, high=1, size=1000),
	'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}
df = pd.DataFrame(data=data, index=date_range)
print(df)
