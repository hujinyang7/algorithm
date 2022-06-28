'''
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数

示例 1：
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3

示例 2:
输入：nums = [1,0,1,1,0,1]
输出：2
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        continuous_count = count = 0
        for each in nums:
            if each == 1:
                count += 1
            else:
                count = 0
            continuous_count = max(continuous_count, count)
        return continuous_count
