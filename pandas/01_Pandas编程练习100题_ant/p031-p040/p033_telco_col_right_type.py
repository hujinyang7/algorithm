# 正确设置数据列的类型
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))

# 从这里开始完成题目
print(df.info())
print(df["TotalCharges"].value_counts())

median = df["TotalCharges"][df["TotalCharges"] != " "].median()
df.loc[df["TotalCharges"] == " ", "TotalCharges"] = median

df["TotalCharges"] = df["TotalCharges"].astype(float)
print()
print(df["TotalCharges"].value_counts())

