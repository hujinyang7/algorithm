# 两只股票数据批量给列名添加前缀
import pandas as pd

bidu = pd.read_csv('stock.BIDU.csv', index_col=0)
iq = pd.read_csv('stock.IQ.csv', index_col=0)

# 从这里开始完成题目

bidu.columns = ["bidu_" + col.lower() for col in bidu.columns]
iq.columns = ["iq_" + col.lower() for col in iq.columns]

print(bidu.head(5))
print()
print(iq.head(5))
