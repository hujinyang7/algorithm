import pandas as pd

df = pd.read_json('market.json')

# pct_change形如：(+1.47%)
df['pct_change'] = df['pct_change'].apply(
	lambda item: float(item[1:-2]))

# 从这里开始完成题目

print(df.iloc[df["pct_change"].argmax()])
print()
print(df.iloc[df["pct_change"].argmin()])
