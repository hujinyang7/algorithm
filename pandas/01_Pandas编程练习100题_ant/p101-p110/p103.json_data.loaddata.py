# 处理Json文件Pandas加载Json文件
import pandas as pd

df = pd.read_json("market.json")

print(df.head(5))
