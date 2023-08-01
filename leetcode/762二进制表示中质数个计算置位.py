'''
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。
计算置位位数 就是二进制表示中 1 的个数。
例如， 21 的二进制表示 10101 有 3 个计算置位。

示例 1：
输入：left = 6, right = 10
输出：4
解释：
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。

示例 2：
输入：left = 10, right = 15
输出：5
解释：
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
'''



class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for item in range(left, right+1):
            contain_1 = (bin(item)[2:]).count('1')
            if self.is_prime_num(contain_1):
                count += 1
        return count

    def is_prime_num(self, num):
        if num == 1:
            return False
        elif num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
