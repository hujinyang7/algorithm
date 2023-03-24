'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        set_str = set(s) if len(s) >= len(t) else set(t)
        for each in set_str:
            if s.count(each) != t.count(each):
                return False
        return True
