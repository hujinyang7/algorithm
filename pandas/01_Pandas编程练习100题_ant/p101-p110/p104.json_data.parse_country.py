# 处理Json文件从字符串解析国家名称
import pandas as pd

df = pd.read_json('market.json')

# 从这里开始完成题目
# profile形如：^AEX (Holandia)
print(df.head(5))

df["country"] = df["profile"].map(
	lambda x: x.split("(")[1].split(")")[0]
)

print(df.head(5))
