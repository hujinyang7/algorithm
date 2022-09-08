# coding:utf-8
# @Time: 8/28/2022
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: Q2.py
# @Project: alvanon_coding_test


# 1.常规解法，通过两次循环迭代遍历，判断 a 中小于 b 元素的个数，时间复杂度O(n^2)
def score_count(team_a: list, team_b: list) -> list:
    res = []
    if not team_a or not team_b:
        return res
    for each in team_b:
        count = 0
        for item in team_a:
            if item <= each:
                count += 1
        if count:
            res.append(count)
    return res


# 2.二分查找法，将 a 列表排序，判断 b 元素在 a 列表中的插入下标，获取前面元素的个数，时间复杂度O(nlogn)
# def score_count(team_a: list, team_b: list) -> list:
#     res = []
#     if not team_a or not team_b:
#         return res
#     team_a.sort()
#     n = len(team_a) - 1
#     for each in team_b:
#         flag = True
#         first, last = 1, n
#         while first <= last:
#             mid = (first + last) // 2
#             if team_a[mid] == each:
#                 res.append(mid + 1)
#                 flag = False
#                 break
#             elif team_a[mid] > each:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#         if flag:
#             res.append(first)
#     return res



if __name__ == '__main__':
    # teamA = [1, 2, 3]
    # teamB = [2, 4]
    # print(score_count(teamA, teamB))   # [2, 3]

    # teamA = [1, 2, 3]
    # teamB = []
    # print(score_count(teamA, teamB))   # []

    # teamA = []
    # teamB = [2, 4]
    # print(score_count(teamA, teamB))   # []

    teamA = [1, 3, 4]
    teamB = [1, 2, 4, 3]
    print(score_count(teamA, teamB))   # [1, 1, 3, 2]

