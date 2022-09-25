# coding:utf-8
# @Time: 2022/9/25
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: Q3.py
# @Project: sf_coding_test


'''
Q:
假如仿真完成后产生大约500万条的记录数据，如何能在消耗内存最少以及时间最短的情况下将数据存储到MYSQL数据库?

A:
1.先将数据预处理为符合存储要求的格式
2.可利用 pandas 将数据进行分段处理
3.利用 celery 通过多个 worker 对分好段的数据进行插库操作
4.但我理解这样消耗内存不是最少的，内存最少和时间最短多少有点相悖
'''
