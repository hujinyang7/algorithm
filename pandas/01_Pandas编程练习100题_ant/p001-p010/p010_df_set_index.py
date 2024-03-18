# 设置DataFrame的索引列

import pandas as pd

data = {
	"姓名": ["小张", "小王", "小李", "小赵"],
	"性别": ["男", "女", "男", "女"],
	"年龄": [18, 19, 20, 18]
}
df = pd.DataFrame(data)

# 从这里开始完成题目
df.set_index("姓名", inplace=True)
print(df)
