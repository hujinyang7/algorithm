'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10-5 的答案都将被视为正确答案。

示例 1：
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

示例 2：
输入：nums = [5], k = 1
输出：5.00000
'''



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp_sum = 0
        largest = float('-inf')
        for i, num in enumerate(nums):
            tmp_sum += num
            if i >= k:
                tmp_sum -= nums[i-k]
            if i >= k-1:
                largest = max(tmp_sum, largest)
        return largest / k
