# 处理Json文件转换字符串到数值列
import pandas as pd

df = pd.read_json('market.json')

# 从这里开始完成题目

print(df.info())
print(df["pct_change"].head(5))

df["pct_change"] = df["pct_change"].map(
	lambda x: float(x[1:-2])
)

print(df.info())
print(df["pct_change"].head(5))

