'''
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
'''



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(' ')
        if len(pattern) != len(slist):
            return False
        map_dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in map_dict:
                if slist[i] in map_dict.values():
                    return False
                map_dict[pattern[i]] = slist[i]
            else:
                if map_dict.get(pattern[i]) != slist[i]:
                    return False
        return True
