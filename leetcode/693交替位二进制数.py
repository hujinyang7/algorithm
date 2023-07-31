'''
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

示例 1：
输入：n = 5
输出：true
解释：5 的二进制表示是：101
示例 2：

输入：n = 7
输出：false
解释：7 的二进制表示是：111.

示例 3：
输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
'''



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n in [0, 1]:
            return True
        bin_num = bin(n)[2:]
        index = 0
        while index < len(bin_num):
            if index % 2 == 0:
                if bin_num[index] != '1':
                    return False
            else:
                if bin_num[index] != '0':
                    return False
            index += 1
        return True
