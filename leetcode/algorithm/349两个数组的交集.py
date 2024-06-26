'''
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return_list = []
        for each in nums1:
            if each in nums2 and each not in return_list:
                return_list.append(each)
        return return_list
