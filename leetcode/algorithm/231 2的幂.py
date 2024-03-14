'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false
如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方 

示例 1：
输入：n = 1
输出：true
解释：20 = 1

示例 2：
输入：n = 16
输出：true
解释：2**4 = 16

示例 3：
输入：n = 3
输出：false

示例 4：
输入：n = 4
输出：true

示例 5：
输入：n = 5
输出：false
'''



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        import math
        x = math.log2(n)
        n = len(str(x).split(".")[1])
        if n > 1:
            return False
        return True
