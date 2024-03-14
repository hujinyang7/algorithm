import pandas as pd

data = {
	'size': ['XL', 'L', 'M', 'L', 'M'],
	'color': ['red', 'green', 'blue', 'green', 'red'],
	'gender': ['female', 'male', 'male', 'female', 'female'],
	'price': [199.0, 89.0, 99.0, 129.0, 79.0],
	'weight': [500, 450, 300, 380, 410],
	'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

# 从这里开始完成题目

df = pd.DataFrame(data)
print(df)
