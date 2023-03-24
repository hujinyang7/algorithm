'''
给定一个  无重复元素 的 有序 整数数组 nums
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x
列表中的每个区间范围 [a,b] 应该按如下格式输出：
"a->b" ，如果 a != b
"a" ，如果 a == b

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 双指针
        left, right = 0, 1
        return_list = []
        while right < len(nums):
            flag = False
            while right < len(nums) and nums[right] - nums[right-1] == 1:
                right += 1
                flag = True
            if flag:
                return_list.append(str(nums[left]) + '->' + str(nums[right-1]))
            else:
                return_list.append(str(nums[left]))
            left = right
            right += 1
        # 处理最后剩一个的情况
        if left == len(nums)-1:
            return_list.append(str(nums[left]))
        return return_list
