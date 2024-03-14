

import numpy as np
import pandas as pd

s = pd.Series(
	np.arange(10, 100, 10),  # 数值：10~90，间隔10
	index=np.arange(101, 110),  # 索引：101~109，间隔1
	dtype='float'  # 类型：float64
)
print(s)
