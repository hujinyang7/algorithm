'''
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
输入: num = 100
输出: "202"

示例 2:
输入: num = -7
输出: "-10"
'''



class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num > 0:
            prefix = ''
        else:
            prefix = '-'
        return_s = ""
        while abs(num):
            num, y = divmod(abs(num), 7)
            return_s = str(y) + return_s
        return prefix + return_s
