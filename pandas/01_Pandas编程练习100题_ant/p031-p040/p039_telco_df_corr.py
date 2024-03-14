
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# 从这里开始完成题目
print(df.head(3))
print(df.info())

print()
print(df.corr())
