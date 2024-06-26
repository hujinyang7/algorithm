'''
你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的
给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数 

示例 1：
输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2

示例 2：
输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3
'''



class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = row = 1
        while True:
            left_count = n - k
            if left_count >= k + 1:
                n -= k
                row += 1
                k += 1
            else:
                break
        return row
