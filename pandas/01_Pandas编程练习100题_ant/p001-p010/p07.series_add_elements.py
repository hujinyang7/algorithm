
import pandas as pd

grades = {"语文": 80, "数学": 90, "英语": 85, "计算机": 100}
data = pd.Series(data=grades)

# 从这里开始完成题目

data = data.append(pd.Series({
	"物理": 88,
	"化学": 95
}))
print(data)

