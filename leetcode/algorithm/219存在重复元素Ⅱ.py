'''
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
'''



class Solution:
    '''用字典保存值和索引'''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        key_to_index = {}
        for i in range(len(nums)):
            if nums[i] in key_to_index and abs(i - key_to_index[nums[i]]) <= k:
                return True
            key_to_index[nums[i]] = i
        return False
