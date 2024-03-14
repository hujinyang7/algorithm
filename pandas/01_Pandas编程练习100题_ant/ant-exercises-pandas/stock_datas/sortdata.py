import pandas as pd

source = "datas/BIDU.csv"
target = "datas/stock.BIDU.csv"

# 这个source文件，来自get_data.py，来自tushare的历史提取
df = pd.read_csv(source, index_col=0)

# 按日期倒序排列
df_sort = df.sort_values(by='trade_date', ascending=False)

# 筛选必须的列
df_sort = df_sort[["trade_date", "open", "high", "low", "close", "vol"]]

# 重命名成标准格式
df_sort = df_sort.rename(columns={
	"trade_date": "Date",
	"open": "Open",
	"high": "High",
	"low": "Low",
	"close": "Close",
	"vol": "Volume",
})

print(df_sort.head(3))
print(df_sort.tail(3))


# 日期变成字符串类型
def format_date(pdate):
	pdate = str(pdate)
	return f"{pdate[:4]}-{pdate[4:6]}-{pdate[6:]}"


df_sort["Date"] = df_sort["Date"].map(format_date)
df_sort["Volume"] = df_sort["Volume"].astype(int)

print(df_sort.head(3))
print(df_sort.info())

df_sort.to_csv(target, index=False)
