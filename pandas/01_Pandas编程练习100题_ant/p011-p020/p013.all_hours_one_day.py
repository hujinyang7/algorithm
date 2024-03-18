# 生成一天中所有的小时
import pandas as pd

#date_range = pd.date_range(start='2021-10-01', periods=24, freq='H')
date_range = pd.date_range(start='2021-10-01',
						   end='2021-10-02',
						   freq='H', closed='left')

print(date_range)
