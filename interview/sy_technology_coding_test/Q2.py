'''
回形输出数组里面的元素
示例 1：
输入：nums = [[1,2,3], [4,5,6]]
输出：[1,2,3,4,5,6]

示例 2：
输入：nums = [[1,2,3], [4,5,6], [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''


def solution(nums):
    return_list = []
    for each in nums:
        for item in each:
            return_list.append(item)
    return return_list


if __name__ == '__main__':
    print(solution([[1,2,3], [4,5,6], [7,8,9]]))
