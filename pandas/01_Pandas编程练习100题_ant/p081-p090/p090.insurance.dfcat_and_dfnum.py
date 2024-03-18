# 保险费用数据集分离类别和数值数据
import pandas as pd

df = pd.read_csv("insurance.csv")
print(df.head())

# 从这里开始完成题目
for column in list(df.select_dtypes(include=["object"]).columns):
	df[column] = df[column].astype("category")

df_cat = df.select_dtypes(include=["category"]).copy()
df_num = df.select_dtypes(include=["float", "int"]).copy()

print(df_cat.head(3))
print(df_num.head(3))
