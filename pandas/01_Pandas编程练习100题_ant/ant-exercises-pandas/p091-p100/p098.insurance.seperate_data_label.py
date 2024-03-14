import pandas as pd

df = pd.read_csv("insurance.csv")

for col in list(df.select_dtypes(include=['object']).columns):
	df[col] = df[col].astype('category')

df_dummies = pd.get_dummies(df, drop_first=True)

# 从这里开始完成题目

print(df_dummies.columns)
data = df_dummies.copy()
target = data.pop("charges")

print(data.head(3))
print()
print(target.head(3))