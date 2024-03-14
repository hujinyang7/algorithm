import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# 从这里开始完成题目
print(df["Churn"].value_counts())
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
print()
print(df["Churn"].value_counts())
