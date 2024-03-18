# 将Series转换成List

import pandas as pd

grades = {"语文": 80, "数学": 90, "英语": 85, "计算机": 100}
data = pd.Series(data=grades)

# 从这里开始完成题目
numbers = data.tolist()
print(numbers)



df = pd.DataFrame({'dates': pd.date_range('2015-01-01', '2015-01-10', freq='12H')})
df.dates.dt.strftime('%H:%S')
print(df)
