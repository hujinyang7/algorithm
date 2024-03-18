# 保险费用数据集查看数值数据列的分布
import pandas as pd

df = pd.read_csv("insurance.csv")

df_num = df.select_dtypes(include=['float', 'int']).copy()

# 从这里开始完成题目

print(df_num.describe())
