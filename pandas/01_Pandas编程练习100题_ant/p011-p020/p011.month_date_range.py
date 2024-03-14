

import pandas as pd

# date_range = pd.date_range(start='2021-10-01', end='2021-10-31')
date_range = pd.date_range(start='2021-10-01', periods=52, freq='W-MON')

print(date_range)
