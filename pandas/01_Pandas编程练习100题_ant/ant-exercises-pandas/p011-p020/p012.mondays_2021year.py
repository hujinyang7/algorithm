import pandas as pd

# date_range = pd.date_range(start='2021-01-01',
#						   end='2021-12-31', freq='W-MON')

date_range = pd.date_range(start='2021-01-01',
						   periods=52, freq='W-MON')

print(date_range)
