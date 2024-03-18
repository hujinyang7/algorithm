# 多维度查看月费字段统
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# 从这里开始完成题目
print(df.columns)
print(df.groupby(["Churn", "PaymentMethod"])["MonthlyCharges"].mean())
