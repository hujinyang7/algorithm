import pandas as pd
from sqlalchemy import create_engine



# 1.pandas中的常用方法
pd.Series()
df = pd.DataFrame()
pd.read_excel()
df.to_excel()
pd.read_sql()
df.loc[]   # 根据行、列的标签值查询
df.iloc[]   # 根据行、列的数字位置查询
pd.merge()
pd.concat()
df.append()

df.iterrows()   #按行迭代， 迭代为(index, Series)对
df.iteritems()   # 按列迭代，迭代为(列名, Series)对
df.itertuples()   # 迭代为index + 列 元组

df.map()  #只用于Series，实现每个值->值的映射
df.apply()  # 用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理
df.applymap()  # 只能用于DataFrame，用于处理该DataFrame的每个元素

df.sort_values()   # 排序
df.sort_index()    # 按 index 排序

df.isnull()   # 检测空值
df.dropna()     # 删除空值
df.fillna({"分数":0})   # 填充空值
df.duplicated()   # 判断是否重复行
df.drop_duplicates(keep="last", subset=['sell_date', 'product'])   # 删除重复行   subset要去重的列名
df.groupby(['A','B'], as_index=False)

# 2
# linux 中查找文件    find ./ -name 0419.txt
# 根据指定内容查找     grep -A 5 'Put up' ./0330.txt -n        -A显示匹配行及其之后的n行    -n显示匹配行号
# 查找到的指定内容存放到另外一个文件夹   grep -A 5 'Put up' ./0330.txt -n > ./o419.txt

# 3.一行代码实现1加到100
sum(range(1, 101))

# 4.可变 list dict set    不可变 int str tuple boole

# 5.排序   快排、归并

# 6.pandas读取一个空表读出的数据类型是什么,如果写一个1又是什么，1.0是什么，1.00是什么
'''
    df = pd.DataFrame({
        'A':['1'],
        'B':[1],
        'C': [1.0],
        'D': [1.00],
    })
    print(df)
    print(df.dtypes)

   A  B    C    D
0  1  1  1.0  1.0
A     object
B      int64
C    float64
D    float64
dtype: object
'''


# def serial_number_six():
#     sql_engine = create_engine(
#             "mysql+pymysql://root:1993hjy@127.0.0.1:3306/it_zn",
#             pool_pre_ping=True,
#             pool_recycle=3600
#         )
#     query_sql = '''select * from it_zn.test'''
#     df_data = pd.read_sql(sql=query_sql, con=sql_engine)
#     print(df_data)
#     print(type(df_data))



# 7. 一行代码实现列表1-100
l = [i for i in range(1, 101)]

# 8.一行代码实现斐波那契数列
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_loop(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

for i in range(10):
    print(fibonacci_recursive(i), end='-')
print('')
for i in range(10):
    print(fibonacci_loop(i), end='|')

# 9   a='123'  a[1]=3  print(a)输出结果是什么
"  会报错： 'str' object does not support item assignment"

# 10 a = (1, 2, [1,3,5], 6) a[2].append(6) 结果是什么
a = (1, 2, [1, 3, 5, 6], 6)     # 延伸考点 a[2] += [6]

# 11 线程进程的区别
'''
1.进程是系统资源分配的基本单位。
2.线程是进程的子任务，并共享进程内资源。
3.一个进程中可以包含若干个线程，但至少有一个线程。
4.协程是比线程更加轻量级的单位，它在单线程里面就能实现任务的切换。就像一个进程里面可以包含多个线程，一个线程里面也可以包含多个协程。
5.进程和线程的切换都是由操作系统控制，切换过程都是 用户态 ——> 内核态 ——> 用户态。而协程则完全由程序控制，切换过程就在用户态中完成，
'''

# 12
'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词，
如果可以输出拆分后的字符串；否则输出None。
并分析代码的时间复杂度。
注：
1.	拆分时可以重复使用字典中的单词；
2.	你可以假设字典中没有重复的单词；
3.	你可以假设字典中没有一个单词是另一个单词的前缀的情况。
示例 1：
输入: s = "anywhere", wordDict = ["any", "where"]
输出: "any where"
示例 2：
输入: s = "anywhere", wordDict = ["what", "where"]
输出: None
'''


def solution(s, word_dict):
    return_str = ""
    begin = 0
    for each in word_dict:
        length = len(each)
        if s[begin: begin + length] == each:
            return_str += s[begin: begin + length]
            return_str += ' '
        begin += length
    if return_str:
        return_str.strip()
        return return_str
    return None


if __name__ == '__main__':
    print(solution("anywhere", ["any", "where"]))
    print(solution("anywhere", ["what", "where"]))


if __name__ == '__main__':
    # serial_number_six()
    # df = pd.DataFrame({
    #     'A':['1'],
    #     'B':[1],
    #     'C': [1.0],
    #     'D': [1.00],
    # })
    print(df)
    print(df.dtypes)

