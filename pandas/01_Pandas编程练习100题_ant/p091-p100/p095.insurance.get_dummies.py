# 保险费用数据集将类别字段转换成01编码
import pandas as pd

df = pd.read_csv("insurance.csv")
for col in list(df.select_dtypes(include=['object']).columns):
	df[col] = df[col].astype('category')

# 从这里开始完成题目

df_dummies = pd.get_dummies(df, drop_first=True)
print(df_dummies.info())
print(df_dummies.head())

