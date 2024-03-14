import pandas as pd

pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)

# 读取csv文件
bidu = pd.read_csv('stock.BIDU.csv', index_col=0)
iq = pd.read_csv('stock.IQ.csv', index_col=0)

# 列名加上前缀，字段名变成小写
bidu.columns = ['bidu_' + col.lower() for col in bidu.columns]
iq.columns = ['iq_' + col.lower() for col in iq.columns]

# 将两个DF，按照日期进行CONCAT
result = pd.concat([bidu, iq], axis=1)

# 提取开盘价和收盘价
quotations = result[['bidu_open', 'bidu_close', 'iq_open', 'iq_close']].copy()

# 计算当日change百分比
quotations['bidu_change'] = (quotations['bidu_close'] / quotations['bidu_open'] - 1) * 100
quotations['iq_change'] = (quotations['iq_close'] / quotations['iq_open'] - 1) * 100

# 从这里开始完成题目
# 计算同时涨、同时跌的信号

print(quotations.head(5))
quotations["similarity_flag"] = (quotations['bidu_change'] * quotations['iq_change'] > 0) * 1
print(quotations.head(5))
