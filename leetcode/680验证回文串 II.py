'''
给你一个字符串 s，最多 可以从中删除一个字符。
请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

示例 1：
输入：s = "aba"
输出：true

示例 2：
输入：s = "abca"
输出：true
解释：你可以删除字符 'c' 。

示例 3：
输入：s = "abc"
输出：false
'''



class Solution:
    def validPalindrome(self, s: str) -> bool:
        is_huiwen_str = lambda s: s == s[::-1]
        beg = 0
        end = len(s)-1
        while beg < end:
            if s[beg] != s[end]:
                return is_huiwen_str(s[0:beg] + s[beg+1:]) or is_huiwen_str(s[0:end] + s[end+1:])
            beg += 1
            end -= 1
        return True
