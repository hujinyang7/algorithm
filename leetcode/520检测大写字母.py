'''
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如 "USA"
单词中所有字母都不是大写，比如 "leetcode"
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false

示例 1：
输入：word = "USA"
输出：true

示例 2：

输入：word = "FlaG"
输出：false
'''



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 如果首字母是小写，那么整个单词必须是小写
        if str.islower(word[0]):
            return str.islower(word)
        else:
            # 首字母大写长度小于3，直接返回True
            if len(word) <= 2:
                return True
            else:
                # 如果第二个字母是小写，剩下的部分也必须小写
                if str.islower(word[1]):
                    return str.islower(word[1:])
                else:
                    # 否则全部为大写
                    return str.isupper(word)
