'''
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
给定一个 整数 n， 如果是完美数，返回 true；否则返回 false。

示例 1：
输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。

示例 2：
输入：num = 7
输出：false
'''



class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        factor = 1
        # 遍历循环和 num/2 循环都会超时
        # 终止条件 factor ** 2 < num
        while factor ** 2 < num:
            if num % factor == 0:
                sum += factor
                if factor != 1:
                    # 如果 factor 是num的因子， 那么 num//factor 也一定是num的因子
                    sum += num // factor
            factor += 1
        return sum == num
