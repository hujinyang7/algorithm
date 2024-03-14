
import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# 从这里开始完成题目
df.sample(10).to_csv("sample10.csv")

