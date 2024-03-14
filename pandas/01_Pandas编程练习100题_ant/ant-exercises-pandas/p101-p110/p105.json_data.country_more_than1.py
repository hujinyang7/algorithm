import pandas as pd

df = pd.read_json('market.json')
# profile形如：^AEX (Holandia)
df['country'] = df['profile'].map(
	lambda x: x.split("(")[1].split(")")[0]
)
print(df.head(5))

# 从这里开始完成题目
df_counts = df["country"].value_counts()
print(df_counts)
print(list(df_counts[df_counts > 1].index))
