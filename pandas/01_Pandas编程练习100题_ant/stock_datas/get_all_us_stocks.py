"""
获取美股列表
"""
# 导入tushare
import pandas as pd
import tushare as ts

# 初始化pro接口
from stock_datas import config

pro = ts.pro_api(config.my_token)

df_list = []
offset = 1
limit = 500
while True:
  # 获取默认美国股票基础信息，单次6000行
  print(f"get stock,offset={offset}, limit={limit}")
  df = pro.us_basic(offset=offset, limit=limit)

  print(f"df.shape={df.shape}")
  if df.shape[0] < limit:
    break
  df_list.append(df)

# 合并所有的内容
pd.concat(df_list).to_csv("datas/all_us_stock.csv")
