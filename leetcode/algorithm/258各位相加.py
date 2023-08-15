'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。 

示例 1:
输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。

示例 2:
输入: num = 0
输出: 0
'''


class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        index = 0
        result = 0
        while index < n:
            result = result + int(str_num[index])
            index += 1
        if result > 9:
            return self.addDigits(result)
        return result
