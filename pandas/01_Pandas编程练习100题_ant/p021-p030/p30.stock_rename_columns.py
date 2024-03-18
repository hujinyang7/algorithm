# 对数据列重命名
import pandas as pd

df = pd.read_csv("./00700.HK.csv")
print(df.head(3))

# 从这里开始完成题目
# df.columns = ["D", "O", "H", "L", "C", "V"]
df.rename(columns={"Date":"D", "Open":"O", "High":"H",
				   "Low":"L", "Close":"C", "Volume":"V"},
		  inplace=True)
print(df.head(3))
