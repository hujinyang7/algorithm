

import pandas as pd

df = pd.DataFrame(
	{
		"姓名": ["小张", "小王", "小李", "小赵"],
		"性别": ["男", "女", "男", "女"],
		"年龄": [18, 19, 20, 18]
	}
)

# print(df)
dd = pd.DataFrame(
	{
		"姓名": ["小1", "小2", "小3", "小4"],
		"性别": ["男", "女", "男", "女"],
		"年龄": [18, 19, 20, 18]
	}
)
re = df.append(dd)
print(re)
