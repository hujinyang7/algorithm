# coding:utf-8
# @Time: 8/28/2022
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: 1.py
# @Project: alvanon_coding_test


def max_num_sort(alist: list) -> list:
    length = len(alist)
    if length <= 2:
        return alist
    rotate_nums_count = (length - 1) // 2   # 倒数个数
    minimum_nums = sorted(alist)[:rotate_nums_count]   # 最小元素数组
    maximal_nums = sorted(alist)[rotate_nums_count:]   # 最大元素数组
    rotate_nums_index = 2   # 倒数元素下标
    item_index = 1
    while minimum_nums:
        alist[rotate_nums_index] = minimum_nums.pop()
        rotate_nums_index += 2
    alist[0] = maximal_nums.pop()
    while maximal_nums:
        alist[item_index] = maximal_nums.pop()
        item_index += 2
    return alist



if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l3 = [3, 7]
    print (max_num_sort(l1))   # [9, 8, 4, 7, 3, 6, 2, 5, 1]
    print (max_num_sort(l2))   # [10, 9, 4, 8, 3, 7, 2, 6, 1, 5]
    print (max_num_sort(l3))   # [3, 7]
