# coding:utf-8
# @Time: 2024/4/1
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @mobile_phone: 18869095465
# @Project: zs_coding_test



# Q1.输入m,n(1 < m < n < 1000000)，返回区间[m,n]内的所有素数的个数
def find_prime_number(m, n):
    prime_nums= []
    for i in range(m, n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)
    return len(prime_nums)



# Q2. 给定一个字符串，找到最长子字符串的长度，要求子字符串中所有字符不重复。
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: 满足条件的最长子字符串为 "abc", 长度为3. 
class Solution():
    def lengthOfLongestSubstring(self, s):
        '''
        方法一，时间复杂度O(n^2)
        定义前后两个指针，通过两层 for 循环获取以每个字符元素为开始的最长子字符串，最后再取总的最长子字符串长度
        '''
        n = len(s)
        if n == len(set(s)):
            # 字符串中无重复元素，直接返回字符串长度
            return n
        pre = 0   # pre指针
        sub_str_list = []
        while pre < n:
            sub_str = s[pre]
            next = pre + 1   # next指针
            while next < n:
                if s[next] not in sub_str:
                    sub_str += s[next]
                    if next == n - 1:
                        # 如果 next 指针走到字符串结尾，直接将当前子字符串加入到 sub_str_list
                        sub_str_list.append(sub_str)
                    next += 1
                else:
                    sub_str_list.append(sub_str)
                    break
            pre += 1
        return max([len(s) for s in sub_str_list])

    def lengthOfLongestSubstring2(self, s):
        '''
        方法二，时间复杂度O(n)
        滑动窗口，通过 begin 和 end(index) 指针构造一个窗口，窗口内所有元素都无重复，
        通过遍历元素移动 end(index) 指针，遇到重复元素移动 begin 指针，然后更新最大长度
        '''
        max_length = 0
        index_dict = {}   # 用字典存储每个字符与其最后一次出现的下标
        begin = 0
        for index, current_str in enumerate(s):
            if current_str in index_dict and index_dict[current_str] >= begin:
                # 如果字符已经在字典中，且其下标大于或等于 begin 指针
                # 移动 begin 指针到重复字符的下一个位置
                begin = index_dict[current_str] + 1
            # 更新字典中的索引
            index_dict[current_str] = index
            # 更新最大长度
            max_length = max(max_length, index - begin + 1)
        return max_length



# Q3.写出排序的过程，给出2个有序的子序列，如何将已有序的子序列合并，得到完全有序的序列，复杂度越低越好；
class CustomSort():
    def normal_sort(self, l_list, r_list):
        '''
        方法一，时间复杂度O(2n)
        通过双指针遍历两个子序列，将两个有序的子序列合并为一个新的整体
        '''
        left_pointer, right_pointer = 0, 0
        result = []
        while left_pointer < len(l_list) and right_pointer < len(r_list):
            if l_list[left_pointer] <= r_list[right_pointer]:
                result.append(l_list[left_pointer])
                left_pointer += 1
            else:
                result.append(r_list[right_pointer])
                right_pointer += 1
        # 循环退出后有一边还会剩一个元素
        result += l_list[left_pointer:]
        result += r_list[right_pointer:]
        return result

    def binary_sort(self, l_list, r_list):
        '''
        方法二，时间复杂度O(n * logn)
        遍历 l_list，通过调用一个二分查找的接口，获取元素在 r_list 的插入位置，将其插入到 r_list，最后返回排序好的 r_list
        '''
        for each in l_list:
            r_list.insert(self.search_insert(r_list, each), each)
        return r_list

    def search_insert(self, nums, target):
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid -1
            else:
                first = mid + 1
        return first



if __name__ == '__main__':
    # Q1
    print(find_prime_number(2, 1000))    # 168

    # Q2
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))   # 3
    print(solution.lengthOfLongestSubstring2("abcabcbb"))  # 3

    # Q3
    l_list = [1,3,7,8,12]
    r_list = [2,5,8,11,20]
    custom_sort = CustomSort()
    print(custom_sort.normal_sort(l_list, r_list))   # [1, 2, 3, 5, 7, 8, 8, 11, 12, 20]
    print(custom_sort.binary_sort(l_list, r_list))   # [1, 2, 3, 5, 7, 8, 8, 11, 12, 20]

