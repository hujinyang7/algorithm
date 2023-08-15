'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
子数组 是数组中的一个连续部分。 

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
'''



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''用两个变量，一个记录最大的和，一个记录当前的和'''
        tmp_sum = float('-inf')
        max_sum = float('-inf')
        for i in range(len(nums)):
            # 当当前和加上当前元素的值大于当前元素，说明最大序列和出现在后续序列中，记录此时的最大值
            if tmp_sum + nums[i] > nums[i]:
                max_sum = max(max_sum, tmp_sum + nums[i])
                tmp_sum = tmp_sum + nums[i]
            else:
                # 当当前和加上当前元素的值小于当前元素，当前最长序列到此为止。以该元素为起点继续找最大子序列,并记录此时的最大值
                max_sum = max(tmp_sum, max_sum, tmp_sum+nums[i], nums[i])
                tmp_sum = nums[i]
        return max_sum
