'''
给定一个非空且只包含非负数的整数数组 nums，数组的 度 的定义是指数组里任一元素出现频数的最大值
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度

示例 1：
输入：nums = [1,2,2,3,1]
输出：2
解释：
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2

示例 2：
输入：nums = [1,2,2,3,1,4,2]
输出：6
解释：
数组的度是 3 ，因为元素 2 重复出现 3 次
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6
'''


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        min_length = float('inf')
        counter = Counter(nums)
        top_list = counter.most_common()
        max_time_nums = []    # 出现频数最大的数
        max_time = top_list[0][1]
        for each in top_list:
            if each [1] == max_time:
                max_time_nums.append(each[0])
        for item in max_time_nums:
            front_count = nums.index(item)   # 前面的数
            rear_count =  list(reversed(nums)).index(item)   # 后面的数
            length = len(nums) - front_count - rear_count
            min_length = min(min_length, length)
        return min_length
