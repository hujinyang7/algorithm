# 处理Json文件pctchange区分存储csv
import pandas as pd

df = pd.read_json('market.json')

# pct_change形如：(+1.47%)
df['pct_change'] = df['pct_change'].apply(
	lambda item: float(item[1:-2]))

# 从这里开始完成题目

df[df['pct_change']>=0].to_json("positive.json", indent=4)
df[df['pct_change']<0].to_json("negative.json", indent=4)
