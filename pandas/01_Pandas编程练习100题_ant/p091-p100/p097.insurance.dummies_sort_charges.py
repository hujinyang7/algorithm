# 保险费用数据集相关性矩阵的筛选排序
import pandas as pd

df = pd.read_csv("insurance.csv")

for col in list(df.select_dtypes(include=['object']).columns):
	df[col] = df[col].astype('category')

df_dummies = pd.get_dummies(df, drop_first=True)

# 从这里开始完成题目

corr = df_dummies.corr()
print(corr[["charges"]].sort_values(by="charges", ascending=False))
