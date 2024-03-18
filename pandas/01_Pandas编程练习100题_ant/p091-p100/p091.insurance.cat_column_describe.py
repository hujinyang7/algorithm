# 保险费用数据集查看类别数据列的分布
import pandas as pd

df = pd.read_csv("insurance.csv")

for col in list(df.select_dtypes(include=['object']).columns):
	df[col] = df[col].astype('category')

df_cat = df.select_dtypes(include=['category']).copy()

# 从这里开始完成题目

print(df_cat.describe())

