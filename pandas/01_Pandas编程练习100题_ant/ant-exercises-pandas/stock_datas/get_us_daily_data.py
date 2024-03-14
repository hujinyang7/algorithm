"""
获取美股数据
"""

# 导入tushare
import time

import pandas as pd
import tushare as ts

# 初始化pro接口
from stock_datas import config

pro = ts.pro_api(config.my_token)

# 百度和爱奇艺股票
stock_code = "BIDU"
# stock_code = "IQ"

df_list = []
dates = [
  (2021, 2021)
]

for begin_year, end_year in dates:
  begin_date, end_date = f"{begin_year}0101", f"{end_year}1231"
  print(begin_date, end_date)

  # 拉取数据
  df = pro.us_daily(ts_code=stock_code,
                    start_date=begin_date,
                    end_date=end_date)

  df_list.append(df)
  time.sleep(5)

pd.concat(df_list).to_csv(f"{stock_code}.csv")
