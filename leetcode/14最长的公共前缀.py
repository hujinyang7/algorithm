'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。 

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        # n = len(strs[0])
        n = min([len(s) for s in strs])
        index = 0
        while index <= n-1:
            flag = True
            prefix = strs[0][index]
            for each in strs[1:]:
                if each[index] != prefix:
                    flag = False
            if flag:
                result += prefix
                index += 1
            else:
                break
        return result
