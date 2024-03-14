import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# 填充 TotalCharges 的缺失值
median = df["TotalCharges"][df["TotalCharges"] != ' '].median()
df.loc[df["TotalCharges"] == ' ', 'TotalCharges'] = median
df["TotalCharges"] = df["TotalCharges"].astype(float)

# 将分类列转换成 Categorical 类型
number_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
for column in number_columns:
	df[column] = df[column].astype(float)
for column in set(df.columns) - set(number_columns):
	df[column] = pd.Categorical(df[column])
print(df.info())

# 从这里开始完成题目
print(df.describe(include=["category"]))
