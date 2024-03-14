
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head(3))

# 从这里开始完成题目
print(df["Churn"].value_counts())
