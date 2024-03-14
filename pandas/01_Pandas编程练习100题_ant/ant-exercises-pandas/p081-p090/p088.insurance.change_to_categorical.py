import pandas as pd

df = pd.read_csv("insurance.csv")
print(df.head())

# 从这里开始完成题目

columns = ["sex", "smoker", "region"]
for column in columns:
	df[column] = df[column].astype("category")

print(df.info())


