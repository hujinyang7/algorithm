'''
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1：
输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

示例 2:
输入： s = "God Ding"
输出："doG gniD"
'''



class Solution:
    def reverseWords(self, s: str) -> str:
        return_str = ''
        list_str = s.split(' ')
        for each in list_str:
            index = len(each) - 1
            while index >= 0:
                return_str += each[index]
                index -= 1
            return_str += ' '
        return return_str.strip()
