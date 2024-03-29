'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现
你可以按任意顺序返回答案。
'''



class Solution:
    # 两次遍历，O(n*n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        count = 0
        for each in nums:
            next_index = count + 1
            while next_index <= len(nums) - 1:
                if each + nums[next_index] == target:
                    return_list.append(count)
                    return_list.append(next_index)
                    return return_list
                else:
                    next_index += 1
            count += 1

def solution(nums, target):
    # 一次遍历，O(n)
    return_list = []
    index = 0
    for each in nums:
        left = target - each
        if left in nums[index+1:]:
            return_list.append(index)
            return_list.append(nums.index(left, index+1))
            return return_list
        index += 1

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(solution(nums, target))
