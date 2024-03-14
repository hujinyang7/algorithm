import pandas as pd

df = pd.read_json('market.json')

# 从这里开始完成题目
# profile形如：^AEX (Holandia)

df["country"] = df["profile"].map(
	lambda x: x.split("(")[1].split(")")[0]
)

print(df.head(5))
