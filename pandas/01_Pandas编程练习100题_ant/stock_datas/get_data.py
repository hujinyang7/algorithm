# 导入tushare
import time

import pandas as pd
import tushare as ts

# 初始化pro接口
from stock_datas import config

pro = ts.pro_api(config.my_token)

stock_code = "00700.HK"
df_list = []
dates = [
	(2004, 2005),
	(2006, 2013),
	(2014, 2021)
]
for begin_year, end_year in dates:
	begin_date, end_date = f"{begin_year}0101", f"{end_year}1231"
	print(begin_date, end_date)

	# 拉取数据
	df = pro.hk_daily(ts_code=stock_code,
					  start_date=begin_date,
					  end_date=end_date)

	df_list.append(df)
	time.sleep(5)

pd.concat(df_list).to_csv(f"{stock_code}.csv")
