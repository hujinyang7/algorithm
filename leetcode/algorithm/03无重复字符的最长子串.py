'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''




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
