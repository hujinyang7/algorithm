'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示

美式键盘 中：
第一行由字符 "qwertyuiop" 组成
第二行由字符 "asdfghjkl" 组成
第三行由字符 "zxcvbnm" 组成

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]
'''



class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return_list = []
        set_one = set('qwertyuiop')
        set_two = set('asdfghjkl')
        set_three = set('zxcvbnm')
        for word in words:
            _word = word.lower()
            if set(_word).issubset(set_one) or set(_word).issubset(set_two) or set(_word).issubset(set_three):
                return_list.append(word)
        return return_list
