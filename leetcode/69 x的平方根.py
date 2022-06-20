'''
给你一个非负整数 x ，计算并返回 x 的 算术平方根
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5

示例 1：
输入：x = 4
输出：2

示例 2：
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去
'''



class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        比较 mid * mid 与 x 的大小，相等则返回 mid，否则去以 mid 为分割点将区间[0, x]
        分成左右区间的两个区间中查找，直到不满足查找条件时退出
        为了防止 mid * mid 太大而发生整型溢出，取 mid 跟 x / mid 进行比较
        '''
        first, last = 1, x
        while first <= last:
            mid = (first + last) // 2
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                last = mid - 1
            else:
                first = mid + 1
        return int(last)
