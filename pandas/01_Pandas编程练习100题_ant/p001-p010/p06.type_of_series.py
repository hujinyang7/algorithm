

import pandas as pd

s = pd.Series(
	data=["001", "002", "003", "004"],
	index=list("abcd")
)

# s = s.astype(int)
s = s.map(int)

print(s)
