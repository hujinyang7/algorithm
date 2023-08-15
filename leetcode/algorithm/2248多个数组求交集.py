'''
给你一个二维整数数组 nums ，其中 nums[i] 是由 不同 正整数组成的一个非空数组，按 升序排列 返回一个数组，数组中的每个元素在 nums 所有数组 中都出现过。

 
示例 1：
输入：nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
输出：[3,4]
解释：
nums[0] = [3,1,2,4,5]，nums[1] = [1,2,3,4]，nums[2] = [3,4,5,6]，在 nums 中每个数组中都出现的数字是 3 和 4 ，所以返回 [3,4] 。

示例 2：
输入：nums = [[1,2,3],[4,5,6]]
输出：[]
解释：
不存在同时出现在 nums[0] 和 nums[1] 的整数，所以返回一个空列表 [] 
'''



class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set_list = []
        for each in nums:
            set_list.append(set(each))
        intersection_set = set()
        default_set = set_list[0]
        flag = True
        for each in set_list:
            if flag:
                intersection_set = each & default_set
            else:
                intersection_set = each & intersection_set
            flag = False
        return_list =  list(intersection_set)
        return_list.sort()
        return return_list
