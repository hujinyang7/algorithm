# 两只股票数据加载CSV文件

import pandas as pd

bidu = pd.read_csv("./stock.BIDU.csv", index_col=0)
iq = pd.read_csv("./stock.IQ.csv", index_col=0)

print(bidu.head(5))
print()
print(iq.head(5))
