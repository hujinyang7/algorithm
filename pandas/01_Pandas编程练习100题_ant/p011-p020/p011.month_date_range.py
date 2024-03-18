# 生成一个月份的所有天

import pandas as pd

# date_range = pd.date_range(start='2021-10-01', end='2021-10-31')
date_range = pd.date_range(start='2021-10-01', periods=52, freq='W-MON')

print(date_range)


df = pd.DataFrame({'dates': pd.date_range('2015-01-01', '2015-01-10', freq='12H')})
print(df)
